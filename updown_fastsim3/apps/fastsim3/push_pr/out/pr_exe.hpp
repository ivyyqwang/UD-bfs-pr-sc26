#ifndef __pr_exe_H__
#define __pr_exe_H__

namespace pr_exe {

    typedef unsigned int EventSymbol;

    constexpr EventSymbol DRAMalloc__dramalloc = 0;
    constexpr EventSymbol DRAMalloc__dramalloc_write_param_return = 1;
    constexpr EventSymbol DRAMalloc__global_broadcast = 2;
    constexpr EventSymbol DRAMalloc__node_broadcast = 3;
    constexpr EventSymbol DRAMalloc__updown_translation_install = 4;
    constexpr EventSymbol DRAMalloc__node_broadcast_return = 5;
    constexpr EventSymbol DRAMalloc__global_broadcast_return = 6;
    constexpr EventSymbol Broadcast__broadcast_global = 7;
    constexpr EventSymbol Broadcast__broadcast_node = 8;
    constexpr EventSymbol Broadcast__broadcast_ud = 9;
    constexpr EventSymbol Broadcast__broadcast_ud_fin = 10;
    constexpr EventSymbol Broadcast__broadcast_node_fin = 11;
    constexpr EventSymbol Broadcast__broadcast_global_fin = 12;
    constexpr EventSymbol Broadcast__broadcast_value_to_scratchpad = 13;
    constexpr EventSymbol splitPageRankMS__map_shuffle_reduce = 14;
    constexpr EventSymbol splitPageRankMS__finish_init_udkvmsr = 15;
    constexpr EventSymbol splitPageRankMS__broadcast_global = 16;
    constexpr EventSymbol splitPageRankMS__broadcast_node = 17;
    constexpr EventSymbol splitPageRankMS__broadcast_ud = 18;
    constexpr EventSymbol splitPageRankMS__broadcast_ud_fin = 19;
    constexpr EventSymbol splitPageRankMS__broadcast_node_fin = 20;
    constexpr EventSymbol splitPageRankMS__broadcast_global_fin = 21;
    constexpr EventSymbol splitPageRankMS__broadcast_value_to_scratchpad = 22;
    constexpr EventSymbol splitPageRankMS__init_input_kvset_on_lane = 23;
    constexpr EventSymbol splitPageRankMS__init_output_kvset_on_lane = 24;
    constexpr EventSymbol splitPageRankMS__init_sp_lane = 25;
    constexpr EventSymbol splitPageRankMS__init_global_master = 26;
    constexpr EventSymbol splitPageRankMS__global_master = 27;
    constexpr EventSymbol splitPageRankMS__cache_flush = 28;
    constexpr EventSymbol splitPageRankMS__cache_flush_return = 29;
    constexpr EventSymbol splitPageRankMS__init_node_master = 30;
    constexpr EventSymbol splitPageRankMS__node_master = 31;
    constexpr EventSymbol splitPageRankMS__termiante_node_master = 32;
    constexpr EventSymbol splitPageRankMS__init_updown_master = 33;
    constexpr EventSymbol splitPageRankMS__updown_master = 34;
    constexpr EventSymbol splitPageRankMS__terminate_updown_master = 35;
    constexpr EventSymbol splitPageRankMS__lane_master_init = 36;
    constexpr EventSymbol splitPageRankMS__lane_master_loop = 37;
    constexpr EventSymbol splitPageRankMS__lane_master_read_partition = 38;
    constexpr EventSymbol splitPageRankMS__lane_master_get_next_return = 39;
    constexpr EventSymbol splitPageRankMS__lane_master_terminate = 40;
    constexpr EventSymbol splitPageRankMS__init_global_snyc = 41;
    constexpr EventSymbol splitPageRankMS__init_node_sync = 42;
    constexpr EventSymbol splitPageRankMS__ud_accumulate = 43;
    constexpr EventSymbol splitPageRankMS__global_sync_return = 44;
    constexpr EventSymbol splitPageRankMS__node_sync_return = 45;
    constexpr EventSymbol splitPageRankMS__ud_entry = 46;
    constexpr EventSymbol splitPageRankMS__ud_delay = 47;
    constexpr EventSymbol splitPageRankMS__kv_map_emit = 48;
    constexpr EventSymbol splitPageRankMS__kv_reduce_emit = 49;
    constexpr EventSymbol splitPageRankMS_output__put_pair_sync = 50;
    constexpr EventSymbol splitPageRankMS__kv_map_return = 51;
    constexpr EventSymbol splitPageRankMS__init_reduce_thread = 52;
    constexpr EventSymbol splitPageRankMS__combine_get_pair = 53;
    constexpr EventSymbol splitPageRankMS__combine_put_pair_ack = 54;
    constexpr EventSymbol splitPageRankMS__kv_reduce_return = 55;
    constexpr EventSymbol splitPageRankMS__combine_flush_lane = 56;
    constexpr EventSymbol splitPageRankMS__combine_flush_ack = 57;
    constexpr EventSymbol splitPageRankMS__kv_map = 58;
    constexpr EventSymbol splitPageRankMS__sibling_rd_return = 59;
    constexpr EventSymbol splitPageRankMS__push_update = 60;
    constexpr EventSymbol splitPageRankMS__rd_nlist_return = 61;
    constexpr EventSymbol InitUpDown__init = 62;
    constexpr EventSymbol InitUpDown__terminate = 63;

} // namespace

#endif