#pragma once

template <class Graph, class RT>
Graph BFS_push_round_on_UpDown(const Graph &g, Graph &frontier, RT *rt,
                               int num_lanes, int iteration_number) {
  std::vector<uint64_t> correct_next_frontier_ids;
  uint64_t correct_M = 0;
  {
    for (uint64_t i = 0; i < frontier.N; i++) {
      auto v = frontier.vertexs[i];
      uint64_t degree = v.degree;
      uint64_t vertex_id = v.vertex_id;
      for (uint64_t j = 0; j < degree; j++) {
        auto neighbor = g.dest(vertex_id, j);
        uint64_t neighbor_distance = g.vertexs[neighbor].scratch1;
        if (neighbor_distance == std::numeric_limits<uint64_t>::max()) {
          correct_next_frontier_ids.push_back(g.dest(vertex_id, j));
        }
      }
    }
    // Remove duplicates
    std::sort(correct_next_frontier_ids.begin(),
              correct_next_frontier_ids.end());
    auto it = std::unique(correct_next_frontier_ids.begin(),
                          correct_next_frontier_ids.end());
    correct_next_frontier_ids.erase(it, correct_next_frontier_ids.end());
    for (auto vertex_id : correct_next_frontier_ids) {
      correct_M += g.vertexs[vertex_id].degree;
    }
  }

  UpDown::networkid_t nwid(0);
  UpDown::operands_t ops(6);
  ops.set_operand(0, frontier.N);
  ops.set_operand(1, frontier.M);
  ops.set_operand(2, frontier.vertexs.data());
  ops.set_operand(3, g.vertexs.data());
  ops.set_operand(4, num_lanes);

  // create an event
  UpDown::event_t event(emEFA::BFS_PUSH__start, nwid, UpDown::CREATE_THREAD,
                        &ops);

  UpDown::word_t flag = 0;
  rt->t2ud_memcpy(
      &flag, sizeof(UpDown::word_t), nwid,
      TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);

  // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

  UpDown::word_t thread_id;
  UpDown::word_t frontier_N;
  UpDown::word_t frontier_M;
  rt->ud2t_memcpy(&thread_id, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 64);
  rt->ud2t_memcpy(&frontier_N, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 72);
  rt->ud2t_memcpy(&frontier_M, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 80);
  std::cout << "frontier size N = " << frontier_N << " M = " << frontier_M
            << "\n";

  if (frontier_N != correct_next_frontier_ids.size()) {
    std::cerr << "frontier_N is wrong got " << frontier_N << " expected "
              << correct_next_frontier_ids.size() << "\n";

    std::cerr << "frontier_M  got " << frontier_M << " expected " << correct_M
              << "\n";
    Graph bad_frontier = Graph::make_empty_for_frontier(rt, g);
    bad_frontier.N = 0;
    bad_frontier.M = 0;
    return bad_frontier;
  }

  if (frontier_M != correct_M) {
    std::cerr << "frontier_M is wrong got " << frontier_M << " expected "
              << correct_M << "\n";
    Graph bad_frontier = Graph::make_empty_for_frontier(rt, g);
    bad_frontier.N = 0;
    bad_frontier.M = 0;
    return bad_frontier;
  }

  auto next_frontier = Graph::make_empty_for_frontier(rt, g);
  next_frontier.alloc_vertexs_for_frontier(frontier_N);
  next_frontier.N = frontier_N;
  next_frontier.M = frontier_M;

  UpDown::operands_t ops2(2);
  ops2.set_operand(0, next_frontier.vertexs.data());
  ops2.set_operand(1, iteration_number);

  // create an event
  UpDown::event_t event2(emEFA::BFS_PUSH__phase3, nwid, thread_id, &ops2);

  flag = 0;
  rt->t2ud_memcpy(
      &flag, sizeof(UpDown::word_t), nwid,
      TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

  // start executing
  rt->send_event(event2);
  rt->start_exec(nwid);

  // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
  bool correct = true;

  if (next_frontier.N != correct_next_frontier_ids.size()) {
    std::cerr << "bad size of next frontier got " << next_frontier.N
              << " expected " << correct_next_frontier_ids.size() << "\n";
    correct = false;
  }

  // first check if the degrees and prefix_sums are correct
  std::vector<uint64_t> next_frontier_ids;
  uint64_t prefix_sum = 0;
  for (uint64_t i = 0; i < next_frontier.N; i++) {
    auto v = next_frontier.vertexs[i];
    uint64_t degree = v.degree;
    uint64_t edges_before = v.edges_before;
    uint64_t vertex_id = v.vertex_id;
    if (edges_before != prefix_sum) {
      std::cerr << "bad prefix sum of edges in new frontier\n";
      correct = false;
    }
    prefix_sum += degree;
    if (degree != g.vertexs[vertex_id].degree) {
      std::cerr << "bad degree in new fontier for vertex " << vertex_id << "\n";
      std::cout << "degree was " << degree << " expected "
                << g.vertexs[vertex_id].degree << "\n";
      correct = false;
    }
    next_frontier_ids.push_back(vertex_id);
  }
  std::sort(next_frontier_ids.begin(), next_frontier_ids.end());
  auto it = std::unique(next_frontier_ids.begin(), next_frontier_ids.end());
  if (it != next_frontier_ids.end()) {
    std::cerr << "frontier has duplicates\n";
    correct = false;
  }
  if (correct_next_frontier_ids != next_frontier_ids) {
    std::cerr << "next frontier has the wrong ids in it\n";
    std::cout << "the lengths are " << next_frontier_ids.size() << " and "
              << correct_next_frontier_ids.size() << "\n";
    correct = false;

    std::vector<uint64_t> only_in_mine;
    std::vector<uint64_t> only_in_correct;

    std::set_difference(next_frontier_ids.begin(), next_frontier_ids.end(),
                        correct_next_frontier_ids.begin(),
                        correct_next_frontier_ids.end(),
                        std::inserter(only_in_mine, only_in_mine.begin()));

    std::set_difference(
        correct_next_frontier_ids.begin(), correct_next_frontier_ids.end(),
        next_frontier_ids.begin(), next_frontier_ids.end(),
        std::inserter(only_in_correct, only_in_correct.begin()));
    std::cout << "only in mine\n";
    for (auto id : only_in_mine) {
      std::cout << id << ", ";
    }
    std::cout << "\n";

    std::cout << "only in correct\n";
    for (auto id : only_in_correct) {
      std::cout << id << ", ";
    }
    std::cout << "\n";
  }

  if (!correct) {
    Graph bad_frontier = Graph::make_empty_for_frontier(rt, g);
    bad_frontier.N = 0;
    bad_frontier.M = 0;
    return bad_frontier;
  }

  return next_frontier;
}

template <class G, class RT>
std::tuple<uint64_t, uint64_t>
BFS_pull_only_on_UpDown_helper(const G &graph, RT *rt, int num_lanes,
                               uint64_t iter) {
  std::vector<uint64_t> correct_next_dist(graph.N);
  {
    for (uint64_t i = 0; i < graph.N; i++) {
      auto &v = graph.vertexs[i];
      uint64_t degree = v.degree;
      if (v.vertex_id != i) {
        std::cerr << "something is wrong with the setup of the vertex ids\n";
        return {0, 0};
      }
      uint64_t my_dist = v.scratch1;
      if (my_dist == std::numeric_limits<uint64_t>::max()) {
        for (uint64_t j = 0; j < degree; j++) {
          auto neighbor = graph.dest(i, j);
          uint64_t neighbor_distance = graph.vertexs[neighbor].scratch1;
          if (neighbor_distance < std::numeric_limits<uint64_t>::max()) {
            my_dist = neighbor_distance + 1;
            break;
          }
        }
      }
      correct_next_dist[i] = my_dist;
    }
  }

  UpDown::networkid_t nwid(0);
  UpDown::operands_t ops(5);
  ops.set_operand(0, graph.N);
  ops.set_operand(1, graph.M);
  ops.set_operand(2, graph.vertexs.data());
  ops.set_operand(3, iter);
  ops.set_operand(4, num_lanes);
  UpDown::event_t event(emEFA::BFS_PULL_main__start, nwid,
                        UpDown::CREATE_THREAD, &ops);

  UpDown::word_t flag = 0;
  rt->t2ud_memcpy(
      &flag, sizeof(UpDown::word_t), nwid,
      TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);

  // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

  UpDown::word_t next_N;
  UpDown::word_t next_M;
  rt->ud2t_memcpy(&next_N, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 64);
  rt->ud2t_memcpy(&next_M, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 72);
  std::cout << "next_N = " << next_N << " next_M = " << next_M << "\n";

  {
    uint64_t count_wrong = 0;
    for (uint64_t i = 0; i < graph.N; i++) {
      if (correct_next_dist[i] != graph.vertexs[i].scratch1) {
        count_wrong += 1;
        std::cout << i << " got " << graph.vertexs[i].scratch1 << " expected "
                  << correct_next_dist[i] << "\n";
      }
    }
    if (count_wrong) {
      std::cerr << "wrong in " << count_wrong << " positions\n";
      return {0, 0};
    }
  }
  return {next_N, next_M};
}

template <class G, class RT>
std::tuple<uint64_t, uint64_t, uint64_t>
BFS_pull_only_multi_on_UpDown_helper(const G &graph, RT *rt, int num_lanes,
                                     uint64_t iter, bool first_iter,
                                     int thread_id = -1) {
  std::vector<uint64_t> correct_next_dist(graph.N);
  {
    for (uint64_t i = 0; i < graph.N; i++) {
      auto &v = graph.vertexs[i];
      uint64_t degree = v.degree;
      if (v.vertex_id != i) {
        std::cerr << "something is wrong with the setup of the vertex ids\n";
        return {0, 0, -1};
      }
      uint64_t my_dist = v.scratch1;
      if (my_dist == std::numeric_limits<uint64_t>::max()) {
        for (uint64_t j = 0; j < degree; j++) {
          auto neighbor = graph.dest(i, j);
          uint64_t neighbor_distance = graph.vertexs[neighbor].scratch1;
          if (neighbor_distance < std::numeric_limits<uint64_t>::max()) {
            my_dist = neighbor_distance + 1;
            break;
          }
        }
      }
      correct_next_dist[i] = my_dist;
    }
  }
  UpDown::networkid_t nwid(0);
  if (first_iter) {
    UpDown::operands_t ops(5);
    ops.set_operand(0, graph.N);
    ops.set_operand(1, graph.M);
    ops.set_operand(2, graph.vertexs.data());
    ops.set_operand(3, iter);
    ops.set_operand(4, num_lanes);
    UpDown::event_t event(emEFA::BFS_PULL_MULTI_main__start, nwid,
                          UpDown::CREATE_THREAD, &ops);

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(
        &flag, sizeof(UpDown::word_t), nwid,
        TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
  } else {
    UpDown::operands_t ops(2);
    ops.set_operand(0, iter);
    UpDown::event_t event(emEFA::BFS_PULL_MULTI_main__run_iter, nwid, thread_id,
                          &ops);

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(
        &flag, sizeof(UpDown::word_t), nwid,
        TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
  }

  // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

  UpDown::word_t next_N;
  UpDown::word_t next_M;
  UpDown::word_t next_thread_id;
  rt->ud2t_memcpy(&next_N, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 64);
  rt->ud2t_memcpy(&next_M, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 72);
  rt->ud2t_memcpy(&next_thread_id, sizeof(UpDown::word_t), nwid,
                  HEAP_OFFSET + 80);
  std::cout << "next_N = " << next_N << " next_M = " << next_M
            << " next_thread_id = " << next_thread_id << "\n";

  {
    uint64_t count_wrong = 0;
    for (uint64_t i = 0; i < graph.N; i++) {
      if (correct_next_dist[i] != graph.vertexs[i].scratch1) {
        count_wrong += 1;
        std::cout << i << " got " << graph.vertexs[i].scratch1 << " expected "
                  << correct_next_dist[i] << "\n";
      }
    }
    if (count_wrong) {
      std::cerr << "wrong in " << count_wrong << " positions\n";
      std::cout << "iter = " << iter << "\n";
      return {0, 0, -1};
    }
  }
  return {next_N, next_M, next_thread_id};
}

template <class G, class RT>
bool BFS_push_only_on_UpDown(const G &graph, unsigned long source, RT *rt,
                             int num_lanes) {
  graph.vertexs[source].scratch1 = 0;
  G frontier = G::make_empty_for_frontier(rt, graph);
  frontier.alloc_vertexs_for_frontier(1);
  frontier.N = 1;
  frontier.M = graph.vertexs[source].degree;
  frontier.vertexs[0].dests = graph.vertexs[source].dests;
  frontier.vertexs[0].degree = graph.vertexs[source].degree;
  frontier.vertexs[0].edges_before = 0;
  frontier.vertexs[0].vertex_id = source;
  unsigned long num_active = frontier.N;

  uint64_t iters = 0;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;
  std::vector<uint64_t> edges_per_iter;
  std::vector<uint64_t> vertices_per_iter;

  while (num_active) {
    // printf("range for graph frontier = %p, %p\n", frontier.vertexs,
    //        frontier.vertexs + frontier.N);
    auto nextFrontier =
        BFS_push_round_on_UpDown(graph, frontier, rt, num_lanes, iters);
    num_active = nextFrontier.N;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    edges_per_iter.push_back(frontier.M);
    vertices_per_iter.push_back(frontier.N);
    sim_ticks = rt->getSimTicks();
    frontier = std::move(nextFrontier);
    iters += 1;
  }
  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.BFS(source);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      // std::cout << "incorrect BFS in position " << i << " got " << got
      //           << " expected " << correct[i] << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "BFS was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "BFS is correct\n";
  std::cout << "### , iteration number, active_set_size, start_outgoing_size, "
               "sim_ticks\n";
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << vertices_per_iter[i] << ", "
              << edges_per_iter[i] << ", " << sim_ticks_per_iter[i] << "\n";
  }
  return true;
}

template <class G, class RT>
bool BFS_pull_only_on_UpDown(const G &graph, unsigned long source, RT *rt,
                             int num_lanes) {
  graph.vertexs[source].scratch1 = 0;
  unsigned long num_active = 1;

  uint64_t iters = 1;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;
  std::vector<uint64_t> edges_per_iter;
  std::vector<uint64_t> vertices_per_iter;

  while (num_active) {
    // printf("range for graph frontier = %p, %p\n", frontier.vertexs,
    //        frontier.vertexs + frontier.N);
    auto [next_N, next_M] =
        BFS_pull_only_on_UpDown_helper(graph, rt, num_lanes, iters);
    num_active = next_N;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    edges_per_iter.push_back(next_M);
    vertices_per_iter.push_back(next_N);
    sim_ticks = rt->getSimTicks();
    iters += 1;
  }
  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.BFS(source);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      // std::cout << "incorrect BFS in position " << i << " got " << got
      //           << " expected " << correct[i] << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "BFS was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "BFS is correct\n";
  std::cout << "### , iteration number, active_set_size, start_outgoing_size, "
               "sim_ticks\n";
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << vertices_per_iter[i] << ", "
              << edges_per_iter[i] << ", " << sim_ticks_per_iter[i] << "\n";
  }
  return true;
}

template <class G, class RT>
bool BFS_push_to_pull_on_UpDown(const G &graph, unsigned long source, RT *rt,
                                int num_lanes) {
  graph.vertexs[source].scratch1 = 0;
  G frontier = G::make_empty_for_frontier(rt, graph);
  frontier.alloc_vertexs_for_frontier(1);
  frontier.N = 1;
  frontier.M = graph.vertexs[source].degree;
  frontier.vertexs[0].dests = graph.vertexs[source].dests;
  frontier.vertexs[0].degree = graph.vertexs[source].degree;
  frontier.vertexs[0].edges_before = 0;
  frontier.vertexs[0].vertex_id = source;
  unsigned long num_active = frontier.N;

  uint64_t iters = 0;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;
  std::vector<uint64_t> edges_per_iter;
  std::vector<uint64_t> vertices_per_iter;

  while (num_active) {
    auto nextFrontier =
        BFS_push_round_on_UpDown(graph, frontier, rt, num_lanes, iters);
    num_active = nextFrontier.N;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    edges_per_iter.push_back(frontier.M);
    vertices_per_iter.push_back(frontier.N);
    sim_ticks = rt->getSimTicks();
    frontier = std::move(nextFrontier);
    iters += 1;
    if (graph.M / frontier.M < 20) {
      // TODO(wheatman) fix this so the two versions don't have different
      // definitions of iters
      iters += 1;
      while (num_active) {
        auto [next_N, next_M] =
            BFS_pull_only_on_UpDown_helper(graph, rt, num_lanes, iters);
        num_active = next_N;
        sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
        edges_per_iter.push_back(next_M);
        vertices_per_iter.push_back(next_N);
        sim_ticks = rt->getSimTicks();
        iters += 1;
      }
    }
  }
  iters -= 1;
  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.BFS(source);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      // std::cout << "incorrect BFS in position " << i << " got " << got
      //           << " expected " << correct[i] << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "BFS was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "BFS is correct\n";
  std::cout << "### , iteration number, active_set_size, start_outgoing_size, "
               "sim_ticks\n";
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << vertices_per_iter[i] << ", "
              << edges_per_iter[i] << ", " << sim_ticks_per_iter[i] << "\n";
  }
  return true;
}

template <class G, class RT>
bool BFS_pull_only_with_multi_on_UpDown(const G &graph, unsigned long source,
                                        RT *rt, int num_lanes) {
  graph.vertexs[source].scratch1 = 0;
  unsigned long num_active = 1;

  uint64_t iters = 1;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;
  std::vector<uint64_t> edges_per_iter;
  std::vector<uint64_t> vertices_per_iter;

  int thread_id = -1;
  while (num_active) {

    auto [next_N, next_M, next_thread_id] =
        BFS_pull_only_multi_on_UpDown_helper(graph, rt, num_lanes, iters,
                                             iters == 1, thread_id);
    if (next_thread_id == -1) {
      std::cerr << "something wrong\n";
      return false;
    }
    thread_id = next_thread_id;
    num_active = next_N;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    edges_per_iter.push_back(next_M);
    vertices_per_iter.push_back(next_N);
    sim_ticks = rt->getSimTicks();
    iters += 1;
  }
  auto [next_N, next_M, next_thread_id] = BFS_pull_only_multi_on_UpDown_helper(
      graph, rt, num_lanes, -1, false, thread_id);
  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.BFS(source);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      std::cout << "incorrect BFS in position " << i << " got "
                << graph.vertexs[i].scratch1 << " expected " << correct[i]
                << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "BFS was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "BFS is correct\n";
  std::cout << "### , iteration number, active_set_size, start_outgoing_size, "
               "sim_ticks\n";
  uint64_t total_sim_ticks = 0;
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << vertices_per_iter[i] << ", "
              << edges_per_iter[i] << ", " << sim_ticks_per_iter[i] << "\n";
    total_sim_ticks += sim_ticks_per_iter[i];
  }
  std::cout << "total sim_ticks = " << total_sim_ticks << "\n";
  return true;
}

template <class G, class RT>
bool BFS_push_to_pull_multi_on_UpDown(const G &graph, unsigned long source,
                                      RT *rt, int num_lanes) {
  graph.vertexs[source].scratch1 = 0;
  G frontier = G::make_empty_for_frontier(rt, graph);
  frontier.alloc_vertexs_for_frontier(1);
  frontier.N = 1;
  frontier.M = graph.vertexs[source].degree;
  frontier.vertexs[0].dests = graph.vertexs[source].dests;
  frontier.vertexs[0].degree = graph.vertexs[source].degree;
  frontier.vertexs[0].edges_before = 0;
  frontier.vertexs[0].vertex_id = source;
  unsigned long num_active = frontier.N;

  uint64_t iters = 0;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;
  std::vector<uint64_t> edges_per_iter;
  std::vector<uint64_t> vertices_per_iter;
  bool first_multi_iteration = true;
  int thread_id = -1;

  while (num_active) {
    auto nextFrontier =
        BFS_push_round_on_UpDown(graph, frontier, rt, num_lanes, iters);
    num_active = nextFrontier.N;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    edges_per_iter.push_back(frontier.M);
    vertices_per_iter.push_back(frontier.N);
    sim_ticks = rt->getSimTicks();
    frontier = std::move(nextFrontier);
    iters += 1;
    if (frontier.M != 0 && graph.M / frontier.M < 20) {
      // TODO(wheatman) fix this so the two versions don't have different
      // definitions of iters
      iters += 1;
      while (num_active) {
        // printf("range for graph frontier = %p, %p\n", frontier.vertexs,
        //        frontier.vertexs + frontier.N);
        auto [next_N, next_M, next_thread_id] =
            BFS_pull_only_multi_on_UpDown_helper(
                graph, rt, num_lanes, iters, first_multi_iteration, thread_id);
        first_multi_iteration = false;
        if (next_thread_id == -1) {
          std::cerr << "something wrong\n";
          return false;
        }
        thread_id = next_thread_id;
        num_active = next_N;
        sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
        edges_per_iter.push_back(next_M);
        vertices_per_iter.push_back(next_N);
        sim_ticks = rt->getSimTicks();
        iters += 1;
      }
    }
  }
  if (first_multi_iteration == false) {
    auto [next_N, next_M, next_thread_id] =
        BFS_pull_only_multi_on_UpDown_helper(graph, rt, num_lanes, -1, false,
                                             thread_id);
    iters -= 1;
  }

  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.BFS(source);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      // std::cout << "incorrect BFS in position " << i << " got " << got
      //           << " expected " << correct[i] << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "BFS was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "BFS is correct\n";
  std::cout << "### , iteration number, active_set_size, start_outgoing_size, "
               "sim_ticks\n";
  uint64_t total_ticks = 0;
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << vertices_per_iter[i] << ", "
              << edges_per_iter[i] << ", " << sim_ticks_per_iter[i] << "\n";
    total_ticks += sim_ticks_per_iter[i];
  }
  std::cout << "total ticks = " << total_ticks << "\n";
  return true;
}