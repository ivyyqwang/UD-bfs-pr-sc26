#include "LMStaticMap.udwh"
#include "basimupdown.h"
#include "dramalloc.hpp"
#include "emEFA.hpp"

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <stdio.h>
#include <string>
#include <string_view>
#include <vector>

#include "algorithms/bfs.hpp"
#include "algorithms/cc.hpp"
#include "algorithms/pr.hpp"

template <typename Runtime> struct Graph {

  template <class T> class DRAM_MALLOC_ARRAY {
    dramalloc::DramAllocator *allocator;
    void *v_adr;

  public:
    DRAM_MALLOC_ARRAY() : allocator(nullptr), v_adr(nullptr) {}
    DRAM_MALLOC_ARRAY(dramalloc::DramAllocator *a, size_t size,
                      size_t blockSize, uint64_t numNodes, uint64_t startNode)
        : allocator(a) {
      if (numNodes == 0) {
        numNodes = 1;
      }
      v_adr = allocator->mm_malloc_global(size * sizeof(T) + 64, blockSize,
                                          numNodes, startNode);
    }
    DRAM_MALLOC_ARRAY(DRAM_MALLOC_ARRAY &&other) {
      allocator = other.allocator;
      other.allocator = nullptr;
      v_adr = other.v_adr;
      other.v_adr = nullptr;
    }
    DRAM_MALLOC_ARRAY &operator=(DRAM_MALLOC_ARRAY &&other) {
      if (this == &other)
        return *this;
      this->allocator = other.allocator;
      other.allocator = nullptr;
      this->v_adr = other.v_adr;
      other.v_adr = nullptr;
      return *this;
    }

    T *data() const { return static_cast<T *>(v_adr); }
    T &operator[](size_t i) const {
      return *reinterpret_cast<T *>(allocator->translate_udva2sa(
          reinterpret_cast<uint64_t>(v_adr) + (i * sizeof(T))));
    }
    static T &get(dramalloc::DramAllocator *a, void *ptr, size_t i) {
      return *reinterpret_cast<T *>(a->translate_udva2sa(
          reinterpret_cast<uint64_t>(ptr) + (i * sizeof(T))));
    }
    void reset() {
      allocator = nullptr;
      v_adr = nullptr;
    }
    void set(void *v) { v_adr = v; }
  };

  class Vertex {
  public:
    uint64_t *dests = nullptr;
    uint64_t degree = 0;
    uint64_t edges_before = 0;
    uint64_t vertex_id = 0;
    // these can be used for different things
    // things like marking a reservation
    // things like current and next values, or multiple different values
    // this is intrusive but allows for different optimizations
    // required to be reset to max at the begining of each algorithm
    uint64_t scratch1 = std::numeric_limits<uint64_t>::max();
    uint64_t scratch2 = std::numeric_limits<uint64_t>::max();
    uint64_t scratch3 = std::numeric_limits<uint64_t>::max();
    uint64_t scratch4 = std::numeric_limits<uint64_t>::max();
  };
  uint64_t N = 0;
  uint64_t M = 0;
  DRAM_MALLOC_ARRAY<Vertex> vertexs = {};
  Runtime *rt = nullptr;
  dramalloc::DramAllocator *allocator = nullptr;

  DRAM_MALLOC_ARRAY<uint64_t> hidden_edges = {};
  uint64_t hidden_edges_size = 0;

  size_t blockSize;
  uint64_t numNodes;
  uint64_t startNode;

  Graph(Runtime *rt_, dramalloc::DramAllocator *a, size_t blockSize_,
        uint64_t numNodes_, uint64_t startNode_)
      : rt(rt_), allocator(a), blockSize(blockSize_), numNodes(numNodes_),
        startNode(startNode_) {
    if (numNodes == 0) {
      numNodes = 1;
    }
  }

  static Graph make_empty_for_frontier(Runtime *rt_, const Graph &g) {
    return Graph(rt_, g.allocator, g.blockSize, g.numNodes, g.startNode);
  }

  ~Graph() {
    // TODO(wheatman) when dram malloc supports free make sure to free the
    // memory
  }

  friend bool operator==(const Graph &lhs, const Graph &rhs) {
    if (lhs.N != rhs.N) {
      return false;
    }
    if (lhs.M != rhs.M) {
      return false;
    }
    if (lhs.vertexs.data() == nullptr || rhs.vertexs.data() == nullptr) {
      if (lhs.vertexs.data() != rhs.vertexs.data()) {
        return false;
      }
    }
    for (uint64_t i = 0; i < lhs.N; i++) {
      if (lhs.vertexs[i].dests == nullptr || rhs.vertexs[i].dests == nullptr) {
        if (lhs.vertexs[i].dests != rhs.vertexs[i].dests) {
          return false;
        }
      }
      if (lhs.vertexs[i].degree != rhs.vertexs[i].degree) {
        return false;
      }
      if (lhs.vertexs[i].edges_before != rhs.vertexs[i].edges_before) {
        return false;
      }
      if (lhs.vertexs[i].vertex_id != rhs.vertexs[i].vertex_id) {
        return false;
      }
      for (uint64_t i = 0; i < lhs.vertexs[i].degree; i++) {
        if (DRAM_MALLOC_ARRAY<uint64_t>::get(lhs.allocator,
                                             lhs.vertexs[i].dests, i) !=
            DRAM_MALLOC_ARRAY<uint64_t>::get(rhs.allocator,
                                             rhs.vertexs[i].dests, i)) {
          return false;
        }
      }
    }
    return true;
  }
  friend inline bool operator!=(const Graph &lhs, const Graph &rhs) {
    return !(lhs == rhs);
  }

  Graph(Graph &&other) {
    N = other.N;
    other.N = 0;
    M = other.M;
    other.M = 0;
    vertexs = std::move(other.vertexs);
    other.vertexs.reset();
    rt = other.rt;
    other.rt = nullptr;
    hidden_edges = std::move(other.hidden_edges);
    other.hidden_edges.reset();
    hidden_edges_size = other.hidden_edges_size;
    other.hidden_edges_size = 0;
    allocator = other.allocator;
    other.allocator = nullptr;

    blockSize = other.blockSize;
    numNodes = other.numNodes;
    startNode = other.startNode;
    other.blockSize = 0;
    other.numNodes = 0;
    other.startNode = 0;
  }
  Graph &operator=(Graph &&other) {
    if (this == &other)
      return *this;

    this->N = other.N;
    other.N = 0;
    this->M = other.M;
    other.M = 0;
    this->vertexs = std::move(other.vertexs);
    other.vertexs.reset();
    this->rt = other.rt;
    other.rt = nullptr;
    this->hidden_edges = std::move(other.hidden_edges);
    other.hidden_edges.reset();
    this->hidden_edges_size = other.hidden_edges_size;
    other.hidden_edges_size = 0;
    this->allocator = other.allocator;
    other.allocator = nullptr;
    this->blockSize = other.blockSize;
    this->numNodes = other.numNodes;
    this->startNode = other.startNode;
    other.blockSize = 0;
    other.numNodes = 0;
    other.startNode = 0;
    return *this;
  }
  Graph(Runtime *rt_, const std::string_view fname, dramalloc::DramAllocator *a,
        size_t blockSize_, uint64_t numNodes_, uint64_t startNode_)
      : rt(rt_), allocator(a), blockSize(blockSize_), numNodes(numNodes_),
        startNode(startNode_) {
    if (numNodes == 0) {
      numNodes = 1;
    }
    if (fname.substr(fname.size() - 4) == ".adj") {
      read_from_adj(fname);
    } else {
      std::cerr << "not implemented yet\n";
    }
  }
  uint64_t &dest(uint64_t source, uint64_t idx) const {
    return *reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(
        reinterpret_cast<uint64_t>(vertexs[source].dests) +
        (idx * sizeof(uint64_t))));
  }

  void alloc_vertexs_for_frontier(uint64_t num_vertexs) {
    vertexs = DRAM_MALLOC_ARRAY<Vertex>(allocator, num_vertexs, blockSize,
                                        numNodes, startNode);
  }

  void read_from_adj(const std::string_view fname) {
    std::fstream s{fname.data(), std::ios::in};
    char buffer[30] = {0};

    s.getline(buffer, 30, '\n');
    std::string header(buffer);
    if (header != "AdjacencyGraph") {
      std::cerr << "bad input file\n";
      return;
    }
    s >> N >> M;

    vertexs =
        DRAM_MALLOC_ARRAY<Vertex>(allocator, N, blockSize, numNodes, startNode);
    hidden_edges_size = M + (8 * N);
    hidden_edges = DRAM_MALLOC_ARRAY<uint64_t>(allocator, hidden_edges_size,
                                               blockSize, numNodes, startNode);
    uint64_t hidden_edges_offset = 0;
    uint64_t last_offset = 0;
    s >> last_offset;
    for (uint64_t i = 1; i < N; i++) {
      uint64_t offset = 0;
      s >> offset;
      vertexs[i - 1].edges_before = last_offset;
      vertexs[i - 1].degree = offset - last_offset;
      vertexs[i - 1].dests = hidden_edges.data() + hidden_edges_offset;
      hidden_edges_offset += vertexs[i - 1].degree;
      if (hidden_edges_offset % 8 != 8) {
        hidden_edges_offset += 8 - (hidden_edges_offset % 8);
      }
      // alloc<uint64_t>(vertexs[i - 1].degree);
      last_offset = offset;
    }
    vertexs[N - 1].edges_before = last_offset;
    vertexs[N - 1].degree = M - last_offset;
    vertexs[N - 1].dests = hidden_edges.data() + hidden_edges_offset;
    // vertexs[N - 1].dests = alloc<uint64_t>(vertexs[N - 1].degree);

    for (uint64_t i = 0; i < N; i++) {
      for (uint64_t j = 0; j < vertexs[i].degree; j++) {
        uint64_t dst = 0;
        s >> dst;
        dest(i, j) = dst;
      }
      vertexs[i].vertex_id = i;
      vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
      vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
      vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
      vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
    }
  }

  void print() {
    std::cout << N << "\n";
    std::cout << M << "\n";
    for (uint64_t i = 0; i < N; i++) {
      std::cout << "Vertex: " << i << "\n";
      for (uint64_t j = 0; j < vertexs[i].degree; j++) {
        std::cout << dest(i, j) << ", ";
      }
      std::cout << "\n";
    }
  }

  std::vector<uint64_t> ConnectedComponents() const {
    std::vector<uint64_t> ids(N);
    for (uint64_t i = 0; i < N; i++) {
      ids[i] = i;
    }
    uint64_t num_active = 1;
    while (num_active != 0) {
      num_active = 0;
      for (uint64_t i = 0; i < N; i++) {
        uint64_t new_id = ids[i];
        bool active = false;
        for (uint64_t j = 0; j < vertexs[i].degree; j++) {
          if (ids[dest(i, j)] < new_id) {
            new_id = ids[dest(i, j)];
            active = true;
          }
        }
        ids[i] = new_id;
        if (active) {
          num_active += 1;
        }
      }
    }
    return ids;
  }

  std::vector<double> PageRank(int max_iters, double epsilon) const {
    std::vector<double> scores(N);
    for (uint64_t i = 0; i < N; i++) {
      scores[i] = 1.0 / N;
    }
    double max_change = std::numeric_limits<double>::max();
    int iters = 0;
    while (max_change > epsilon && iters < max_iters) {
      std::vector<double> new_scores = scores;
      max_change = 0;
      for (uint64_t i = 0; i < N; i++) {
        double new_score = 0;
        for (uint64_t j = 0; j < vertexs[i].degree; j++) {
          new_score += scores[dest(i, j)] / vertexs[dest(i, j)].degree;
        }
        if (vertexs[i].degree == 0) {
          new_score = scores[i];
        }
        double difference = std::abs(new_score - scores[i]);
        max_change = std::max(max_change, difference);
        new_scores[i] = new_score;
      }
      scores = new_scores;
      iters = iters + 1;
    }
    return scores;
  }

  std::pair<std::vector<uint64_t>, uint64_t>
  BFS_iter(const std::vector<uint64_t> &distances) const {
    std::vector<uint64_t> next(distances.size());
    uint64_t num_active = 0;
    for (uint64_t i = 0; i < N; i++) {
      uint64_t new_distance = distances[i];
      bool active = false;
      for (uint64_t j = 0; j < vertexs[i].degree; j++) {
        if (distances[dest(i, j)] != std::numeric_limits<uint64_t>::max() &&
            distances[dest(i, j)] + 1 < new_distance) {
          new_distance = distances[dest(i, j)] + 1;
          active = true;
        }
      }
      next[i] = new_distance;
      if (active) {
        num_active += 1;
      }
    }
    return {next, num_active};
  }

  std::vector<uint64_t> BFS(uint64_t source) const {
    std::vector<uint64_t> distances(
        N, (uint64_t)std::numeric_limits<uint64_t>::max());
    distances[source] = 0;
    std::vector<uint64_t> frontier;
    frontier.push_back(source);
    while (!frontier.empty()) {
      std::vector<uint64_t> next_frontier;
      for (auto vertex : frontier) {
        for (uint64_t j = 0; j < vertexs[vertex].degree; j++) {
          auto new_neighbor_distance = distances[vertex] + 1;
          if (new_neighbor_distance < distances[dest(vertex, j)]) {
            distances[dest(vertex, j)] = new_neighbor_distance;
            next_frontier.push_back(dest(vertex, j));
          }
        }
      }
      std::swap(frontier, next_frontier);
    }
    return distances;
  }
};
