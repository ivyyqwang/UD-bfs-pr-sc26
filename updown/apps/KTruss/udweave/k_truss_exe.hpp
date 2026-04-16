#ifndef __k_truss_exe_H__
#define __k_truss_exe_H__

namespace k_truss_exe {

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
    constexpr EventSymbol vertex_filter_master__launch = 14;
    constexpr EventSymbol vertex_filter_master__receive_dram = 15;
    constexpr EventSymbol vertex_filter_master__v1_return = 16;
    constexpr EventSymbol vertex_filter_master__v1_neighs_count = 17;
    constexpr EventSymbol vertex_filter_master__v1_neighs = 18;
    constexpr EventSymbol vertex_filter_master__write_return = 19;
    constexpr EventSymbol vertex_filter_master_local__launch = 20;
    constexpr EventSymbol vertex_filter_master_local__receive_dram = 21;
    constexpr EventSymbol vertex_filter_master_local__v1_return = 22;
    constexpr EventSymbol vertex_filter_master_local__v1_neighs_count = 23;
    constexpr EventSymbol vertex_filter_master_local__v1_neighs = 24;
    constexpr EventSymbol vertex_filter_master_local__write_return = 25;
    constexpr EventSymbol vertex_master__launch = 26;
    constexpr EventSymbol vertex_master__v1_return = 27;
    constexpr EventSymbol vertex_master__v1_neighs = 28;
    constexpr EventSymbol intersection_launcher__intersection_init = 29;
    constexpr EventSymbol intersection_launcher__receive = 30;
    constexpr EventSymbol intersection_launcher__receive_from_dram = 31;
    constexpr EventSymbol intersection_launcher__intersection_term = 32;
    constexpr EventSymbol intersection_launcher__cache_write_finish = 33;
    constexpr EventSymbol intersection_launcher__send_to_worker_thread2 = 34;
    constexpr EventSymbol intersection_launcher__send_to_worker_thread5 = 35;
    constexpr EventSymbol intersection_launcher__v1v2_write_return = 36;
    constexpr EventSymbol intersection_launcher__add_one = 37;
    constexpr EventSymbol intersection_launcher__add_value = 38;
    constexpr EventSymbol intersection_launcher__add_return = 39;
    constexpr EventSymbol intersection_launcher__write_back_cache = 40;
    constexpr EventSymbol intersection_launcher__intersection_end = 41;
    constexpr EventSymbol intersection_cache__add_val_dram_write = 42;
    constexpr EventSymbol intersection_cache__add_value_dram_write_return = 43;
    constexpr EventSymbol intersection_cache__add_value_dram_read_return = 44;
    constexpr EventSymbol master_launcher__init = 45;
    constexpr EventSymbol master_launcher__launch_v = 46;
    constexpr EventSymbol master_launcher__read_master_dram_length = 47;
    constexpr EventSymbol master_launcher__receive_dram = 48;
    constexpr EventSymbol master_launcher__read_remote_data = 49;
    constexpr EventSymbol master_launcher__read_master_dram_length_compact = 50;
    constexpr EventSymbol master_launcher__receive_dram_remote = 51;
    constexpr EventSymbol master_launcher__vertex_term = 52;
    constexpr EventSymbol master_launcher__relaunch = 53;
    constexpr EventSymbol master_launcher__write_return = 54;
    constexpr EventSymbol master_launcher__all_launched = 55;
    constexpr EventSymbol master_launcher__reduce_num_int = 56;
    constexpr EventSymbol master_launcher__send_to_master_thread1 = 57;
    constexpr EventSymbol master_launcher__send_to_master_thread2 = 58;
    constexpr EventSymbol filter_launcher__start = 59;
    constexpr EventSymbol filter_launcher__read_master_dram_length = 60;
    constexpr EventSymbol filter_launcher__vertex_term = 61;
    constexpr EventSymbol filter_launcher__write_return = 62;
    constexpr EventSymbol main_master__init_tc = 63;
    constexpr EventSymbol main_master__init_done = 64;
    constexpr EventSymbol main_master__send_to_global_master_thread = 65;
    constexpr EventSymbol main_master__start = 66;
    constexpr EventSymbol main_master__v_launcher_done = 67;
    constexpr EventSymbol main_master__v_all_launched = 68;
    constexpr EventSymbol main_master__int_launcher_done = 69;
    constexpr EventSymbol main_master__int_all_launched = 70;
    constexpr EventSymbol main_master__tc_launcher_done = 71;
    constexpr EventSymbol main_master__tc_all_launched = 72;
    constexpr EventSymbol main_master__cache_launcher_done = 73;
    constexpr EventSymbol main_master__cache_all_launched = 74;
    constexpr EventSymbol main_master__filter_launcher_done = 75;
    constexpr EventSymbol dram_copy__send_reads = 76;
    constexpr EventSymbol dram_copy__read_returns = 77;
    constexpr EventSymbol dram_copy__write_returns = 78;

} // namespace

#endif