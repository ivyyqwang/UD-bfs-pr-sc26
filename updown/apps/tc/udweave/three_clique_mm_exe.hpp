#ifndef __three_clique_mm_exe_H__
#define __three_clique_mm_exe_H__

namespace three_clique_mm_exe {

    typedef unsigned int EventSymbol;

    constexpr EventSymbol DRAMalloc__dramalloc = 0;
    constexpr EventSymbol DRAMalloc__dramalloc_write_param_return = 1;
    constexpr EventSymbol DRAMalloc__global_broadcast = 2;
    constexpr EventSymbol DRAMalloc__node_broadcast = 3;
    constexpr EventSymbol DRAMalloc__updown_translation_install = 4;
    constexpr EventSymbol DRAMalloc__updown_translation_free = 5;
    constexpr EventSymbol DRAMalloc__node_broadcast_return = 6;
    constexpr EventSymbol DRAMalloc__global_broadcast_return = 7;
    constexpr EventSymbol v1v2intersection__launch = 8;
    constexpr EventSymbol v1v2intersection__vert_return = 9;
    constexpr EventSymbol v1v2intersection__intersect_lists = 10;
    constexpr EventSymbol v1v2intersection__lista_ret_1 = 11;
    constexpr EventSymbol v1v2intersection__listb_ret_1 = 12;
    constexpr EventSymbol v1v2intersection__intersect_ab = 13;
    constexpr EventSymbol vertex_master__launch = 14;
    constexpr EventSymbol vertex_master__v1_return = 15;
    constexpr EventSymbol vertex_master__v1_neighs = 16;
    constexpr EventSymbol intersection_launcher__intersection_init = 17;
    constexpr EventSymbol intersection_launcher__receive = 18;
    constexpr EventSymbol intersection_launcher__receive_from_dram = 19;
    constexpr EventSymbol intersection_launcher__intersection_term = 20;
    constexpr EventSymbol intersection_launcher__get_tc = 21;
    constexpr EventSymbol intersection_launcher__send_to_worker_thread2 = 22;
    constexpr EventSymbol intersection_launcher__send_to_worker_thread4 = 23;
    constexpr EventSymbol intersection_launcher__v1v2_write_return = 24;
    constexpr EventSymbol master_launcher__init = 25;
    constexpr EventSymbol master_launcher__read_master_dram_length = 26;
    constexpr EventSymbol master_launcher__intersection_init_done = 27;
    constexpr EventSymbol master_launcher__launch_v = 28;
    constexpr EventSymbol master_launcher__receive_dram = 29;
    constexpr EventSymbol master_launcher__vertex_term = 30;
    constexpr EventSymbol master_launcher__relaunch = 31;
    constexpr EventSymbol master_launcher__all_launched = 32;
    constexpr EventSymbol master_launcher__reduce_num_int = 33;
    constexpr EventSymbol master_launcher__send_to_master_thread1 = 34;
    constexpr EventSymbol main_master__init_tc = 35;
    constexpr EventSymbol main_master__init_done = 36;
    constexpr EventSymbol main_master__send_to_global_master_thread = 37;
    constexpr EventSymbol main_master__start = 38;
    constexpr EventSymbol main_master__v_launcher_done = 39;
    constexpr EventSymbol main_master__v_all_launched = 40;
    constexpr EventSymbol main_master__int_launcher_done = 41;
    constexpr EventSymbol main_master__int_all_launched = 42;
    constexpr EventSymbol main_master__tc_launcher_done = 43;
    constexpr EventSymbol dram_copy__send_reads = 44;
    constexpr EventSymbol dram_copy__read_returns = 45;
    constexpr EventSymbol dram_copy__write_returns = 46;

} // namespace

#endif