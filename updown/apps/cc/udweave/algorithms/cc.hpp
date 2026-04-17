#pragma once

template <class G, class RT>
std::tuple<uint64_t, uint64_t, uint64_t>
CC_pull_only_multi_on_UpDown_helper(const G &graph, RT *rt, int num_lanes,
                                    int thread_id = -1) {

  UpDown::networkid_t nwid(0);
  if (thread_id == -1) {
    UpDown::operands_t ops(4);
    ops.set_operand(0, graph.N);
    ops.set_operand(1, graph.M);
    ops.set_operand(2, graph.vertexs.data());
    ops.set_operand(3, num_lanes);
    UpDown::event_t event(emEFA::CC_PULL_MULTI_main__start, nwid,
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
    ops.set_operand(0, 0);
    UpDown::event_t event(emEFA::CC_PULL_MULTI_main__run_iter, nwid, thread_id,
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

  UpDown::word_t num_updated;
  UpDown::word_t min_written;
  UpDown::word_t next_thread_id;
  rt->ud2t_memcpy(&num_updated, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 64);
  rt->ud2t_memcpy(&min_written, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 72);
  rt->ud2t_memcpy(&next_thread_id, sizeof(UpDown::word_t), nwid,
                  HEAP_OFFSET + 80);
  std::cout << "num_updated = " << num_updated
            << " min_written = " << min_written
            << " next_thread_id = " << next_thread_id << "\n";

  if (num_updated == 0) {
    UpDown::operands_t ops(2);
    ops.set_operand(0, -1UL);
    UpDown::event_t event(emEFA::CC_PULL_MULTI_main__run_iter, nwid,
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

  return {num_updated, min_written, next_thread_id};
}

template <class G, class RT> bool CC_on_UpDown(G &graph, RT rt, int num_lanes) {

  uint64_t iters = 1;
  uint64_t sim_ticks = rt->getSimTicks();

  std::vector<uint64_t> sim_ticks_per_iter;

  int thread_id = -1;
  unsigned long num_active = 1;
  while (num_active) {
    // printf("range for graph frontier = %p, %p\n", frontier.vertexs,
    //        frontier.vertexs + frontier.N);

    auto [num_written, min_label_written, next_thread_id] =
        CC_pull_only_multi_on_UpDown_helper(graph, rt, num_lanes, thread_id);
    if (next_thread_id == -1) {
      std::cerr << "something wrong\n";
      return false;
    }
    thread_id = next_thread_id;
    num_active = num_written;
    sim_ticks_per_iter.push_back(rt->getSimTicks() - sim_ticks);
    sim_ticks = rt->getSimTicks();
    iters += 1;
  }
  std::cout << "took " << iters << " iterations\n";
  auto correct = graph.ConnectedComponents();
  uint64_t wrong_positions = 0;
  for (uint64_t i = 0; i < graph.N; i++) {
    if (correct[i] != graph.vertexs[i].scratch1) {
      std::cout << "incorrect CC in position " << i << " got "
                << graph.vertexs[i].scratch1 << " expected " << correct[i]
                << "\n";
      wrong_positions += 1;
    }
  }
  if (wrong_positions) {
    std::cerr << "CC was wrong in " << wrong_positions << " positions \n";
    return false;
  }
  std::cout << "CC is correct\n";
  std::cout << "### , iteration number, sim_ticks\n";
  uint64_t total_sim_ticks = 0;
  for (uint64_t i = 0; i < sim_ticks_per_iter.size(); i++) {
    std::cout << "###, " << i << ", " << sim_ticks_per_iter[i] << "\n";
    total_sim_ticks += sim_ticks_per_iter[i];
  }
  std::cout << "total sim_ticks = " << total_sim_ticks << "\n";
  return true;
}