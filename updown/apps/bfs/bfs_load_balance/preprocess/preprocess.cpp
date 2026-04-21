
#include <fstream>
#include <limits>
#include <vector>

#include <climits>
#include <stdint.h>
#include <iostream>
#include <bit>
#include <algorithm>


std::vector<std::vector<uint32_t>> readGraph(const std::string &filename) {
  std::ifstream infile(filename);

  if (!infile.is_open()) {
    std::cerr << "Error opening file: " << filename << std::endl;
    return {};
  }

  std::vector<std::vector<uint32_t>> adjacencyList;
  uint32_t src, dest;

  // int limit = 0;
  while (infile >> src >> dest) {
    if (src == dest) {
      continue;
    }
    if (std::max(src, dest) >= adjacencyList.size()) {
      adjacencyList.resize(std::max(src, dest) + 1);
    }
    adjacencyList[src].push_back(dest);
    adjacencyList[dest].push_back(src);
    // if (limit > 10000000) {
    //   break;
    // }
    // limit += 1;
  }

  infile.close();

  std::cout << "done reading in the graph\n";

  for (auto &edges : adjacencyList) {
    std::sort(edges.begin(), edges.end());
    auto last = std::unique(edges.begin(), edges.end());
    edges.erase(last, edges.end());
  }
  return adjacencyList;
}

bool write_graph(const std::vector<std::vector<uint32_t>> &graph,
                 const std::string &filename) {
  size_t M = 0;
  std::vector<size_t> prefix_sum;
  for (size_t i = 0; i < graph.size(); i++) {
    prefix_sum.push_back(M);
    M += graph[i].size();
  }
  prefix_sum.push_back(M);
  std::cout << "starting to write the graph\n";

  std::ofstream myfile;
  myfile.open(filename);
  myfile << "AdjacencyGraph\n";

  myfile << graph.size() << "\n";

  myfile << M << "\n";
  for (uint64_t i = 0; i < graph.size(); i++) {
    myfile << prefix_sum[i] << "\n";
  }
  for (uint64_t i = 0; i < graph.size(); i++) {
    for (const auto &dest : graph[i]) {
      myfile << dest << "\n";
    }
  }
  myfile.close();
  return true;
}

int main([[maybe_unused]] int32_t argc, char *argv[]) {

  auto graph = readGraph(argv[1]);
  write_graph(graph, argv[2]);
}