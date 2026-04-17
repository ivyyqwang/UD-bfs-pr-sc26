#pragma once

template <class G, class RT>
std::vector<uint64_t>
PR_pull_only_multi_on_UpDown_helper(const G &graph, int max_iters,
                                    double epsilon, RT *rt, int num_lanes) {

  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;

  UpDown::networkid_t nwid(0);
  double max_change;
  UpDown::operands_t ops(4);
  ops.set_operand(0, graph.N);
  ops.set_operand(1, graph.M);
  ops.set_operand(2, graph.vertexs.data());
  ops.set_operand(3, num_lanes);
  UpDown::event_t event(emEFA::PR_PULL_MULTI_main__start, nwid,
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
  sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
  sim_ticks = rt->getSimTicks();

  UpDown::word_t next_thread_id;
  rt->ud2t_memcpy(&max_change, sizeof(double), nwid, HEAP_OFFSET + 64);
  rt->ud2t_memcpy(&next_thread_id, sizeof(UpDown::word_t), nwid,
                  HEAP_OFFSET + 80);
  std::cout << "max_change = " << max_change
            << " next_thread_id = " << next_thread_id << "\n";

  int iters = 1;

  while (max_change > epsilon && iters < max_iters) {
    UpDown::operands_t ops(2);
    ops.set_operand(0, 0);
    UpDown::event_t event(emEFA::PR_PULL_MULTI_main__run_iter, nwid,
                          next_thread_id, &ops);

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(
        &flag, sizeof(UpDown::word_t), nwid,
        TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);

    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    sim_ticks = rt->getSimTicks();

    rt->ud2t_memcpy(&max_change, sizeof(double), nwid, HEAP_OFFSET + 64);
    rt->ud2t_memcpy(&next_thread_id, sizeof(UpDown::word_t), nwid,
                    HEAP_OFFSET + 80);
    std::cout << "max_change = " << max_change
              << " next_thread_id = " << next_thread_id << "\n";
    iters += 1;
  }
  {
    UpDown::operands_t ops(2);
    ops.set_operand(0, -1UL);
    UpDown::event_t event(emEFA::PR_PULL_MULTI_main__run_iter, nwid,
                          next_thread_id, &ops);

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(
        &flag, sizeof(UpDown::word_t), nwid,
        TOP_FLAG_OFFSET); // copy the value of flag to the SP of NWID 0

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
  }
  sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
  sim_ticks = rt->getSimTicks();

  return sim_ticks_per_iter;
}

bool is_close(double a, double b, double epsilon) {
  if (a > b) {
    return (a - b) < epsilon;
  }
  return (b - a) < epsilon;
}

template <class To, class From>
std::enable_if_t<sizeof(To) == sizeof(From) &&
                     std::is_trivially_copyable_v<From> &&
                     std::is_trivially_copyable_v<To>,
                 To>
// constexpr support needs compiler magic
bit_cast(const From &src) noexcept {
  static_assert(std::is_trivially_constructible_v<To>,
                "This implementation additionally requires "
                "destination type to be trivially constructible");

  To dst;
  std::memcpy(&dst, &src, sizeof(To));
  return dst;
}

template <class G, class RT>
bool PR_on_UpDown(G &graph, int max_iters, double epsilon, RT rt,
                  int num_lanes) {

  uint64_t iters = 1;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter =
      PR_pull_only_multi_on_UpDown_helper(graph, max_iters, epsilon, rt,
                                          num_lanes);

  std::cout << "took " << sim_ticks_per_iter.size() - 1 << " iterations\n";
  auto correct = graph.PageRank(max_iters, epsilon);
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    double got = bit_cast<double, uint64_t>(graph.vertexs[i].scratch1);
    if (!is_close(correct[i], got, epsilon)) {
      std::cout << "incorrect PR in position " << i << " got " << got
                << " expected " << correct[i] << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "PR was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "PR is correct\n";
  std::cout << "### , iteration number, sim_ticks\n";
  uint64_t total_sim_ticks = 0;
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << sim_ticks_per_iter[i] << "\n";
    total_sim_ticks += sim_ticks_per_iter[i];
  }
  std::cout << "total sim_ticks = " << total_sim_ticks << "\n";
  return true;
}
