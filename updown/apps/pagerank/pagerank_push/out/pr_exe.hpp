#ifndef __pr_exe_H__
#define __pr_exe_H__

namespace pr_exe {

    typedef unsigned int EventSymbol;

    constexpr EventSymbol DRAMalloc__dramalloc = 0;
    constexpr EventSymbol DRAMalloc__dramalloc_write_param_return = 1;
    constexpr EventSymbol DRAMalloc__global_broadcast = 2;
    constexpr EventSymbol DRAMalloc__node_broadcast = 3;
    constexpr EventSymbol DRAMalloc__updown_translation_install = 4;
    constexpr EventSymbol DRAMalloc__updown_translation_free = 5;
    constexpr EventSymbol DRAMalloc__node_broadcast_return = 6;
    constexpr EventSymbol DRAMalloc__global_broadcast_return = 7;
    constexpr EventSymbol KnaryBroadcastNode__global_init = 8;
    constexpr EventSymbol KnaryBroadcastNode__global_sync = 9;
    constexpr EventSymbol KnaryBroadcastNode__broadcast_nodes = 10;
    constexpr EventSymbol KnaryBroadcastNode__node_sync = 11;
    constexpr EventSymbol GlobalSync__global_init = 12;
    constexpr EventSymbol GlobalSync__global_sync = 13;
    constexpr EventSymbol NodeSync__node_bcst = 14;
    constexpr EventSymbol NodeSync__node_sync = 15;
    constexpr EventSymbol UpdownSync__ud_entry = 16;
    constexpr EventSymbol UpdownSync__ud_loop = 17;
    constexpr EventSymbol UpdownSync__ud_accum = 18;
    constexpr EventSymbol Broadcast__broadcast_global = 19;
    constexpr EventSymbol Broadcast__broadcast_node = 20;
    constexpr EventSymbol Broadcast__broadcast_ud = 21;
    constexpr EventSymbol Broadcast__broadcast_ud_fin = 22;
    constexpr EventSymbol Broadcast__broadcast_node_fin = 23;
    constexpr EventSymbol Broadcast__broadcast_global_fin = 24;
    constexpr EventSymbol Broadcast__tree_broadcast_node_dst = 25;
    constexpr EventSymbol Broadcast__broadcast_value_to_scratchpad = 26;
    constexpr EventSymbol splitPageRankMS__map_shuffle_reduce = 27;
    constexpr EventSymbol splitPageRankMS__finish_init_udkvmsr = 28;
    constexpr EventSymbol splitPageRankMS__broadcast_global = 29;
    constexpr EventSymbol splitPageRankMS__broadcast_node = 30;
    constexpr EventSymbol splitPageRankMS__broadcast_ud = 31;
    constexpr EventSymbol splitPageRankMS__broadcast_ud_fin = 32;
    constexpr EventSymbol splitPageRankMS__broadcast_node_fin = 33;
    constexpr EventSymbol splitPageRankMS__broadcast_global_fin = 34;
    constexpr EventSymbol splitPageRankMS__tree_broadcast_node_dst = 35;
    constexpr EventSymbol splitPageRankMS__broadcast_value_to_scratchpad = 36;
    constexpr EventSymbol splitPageRankMS__init_input_kvset_on_lane = 37;
    constexpr EventSymbol splitPageRankMS__init_output_kvset_on_lane = 38;
    constexpr EventSymbol splitPageRankMS__init_sp_lane = 39;
    constexpr EventSymbol splitPageRankMS__init_global_master = 40;
    constexpr EventSymbol splitPageRankMS__global_master = 41;
    constexpr EventSymbol splitPageRankMS__cache_flush = 42;
    constexpr EventSymbol splitPageRankMS__cache_flush_return = 43;
    constexpr EventSymbol splitPageRankMS__init_node_master = 44;
    constexpr EventSymbol splitPageRankMS__node_master = 45;
    constexpr EventSymbol splitPageRankMS__termiante_node_master = 46;
    constexpr EventSymbol splitPageRankMS__init_updown_master = 47;
    constexpr EventSymbol splitPageRankMS__updown_master = 48;
    constexpr EventSymbol splitPageRankMS__terminate_updown_master = 49;
    constexpr EventSymbol splitPageRankMS__lane_master_init = 50;
    constexpr EventSymbol splitPageRankMS__lane_master_loop = 51;
    constexpr EventSymbol splitPageRankMS__lane_master_read_partition = 52;
    constexpr EventSymbol splitPageRankMS__lane_master_get_next_return = 53;
    constexpr EventSymbol splitPageRankMS__lane_master_terminate = 54;
    constexpr EventSymbol splitPageRankMS__init_global_snyc = 55;
    constexpr EventSymbol splitPageRankMS__init_node_sync = 56;
    constexpr EventSymbol splitPageRankMS__ud_accumulate = 57;
    constexpr EventSymbol splitPageRankMS__global_sync_return = 58;
    constexpr EventSymbol splitPageRankMS__node_sync_return = 59;
    constexpr EventSymbol splitPageRankMS__ud_entry = 60;
    constexpr EventSymbol splitPageRankMS__ud_delay = 61;
    constexpr EventSymbol splitPageRankMS__kv_map_emit = 62;
    constexpr EventSymbol splitPageRankMS__kv_reduce_emit = 63;
    constexpr EventSymbol splitPageRankMS_output__put_pair_sync = 64;
    constexpr EventSymbol splitPageRankMS__kv_map_return = 65;
    constexpr EventSymbol splitPageRankMS__init_reduce_thread = 66;
    constexpr EventSymbol splitPageRankMS__combine_get_pair = 67;
    constexpr EventSymbol splitPageRankMS__combine_put_pair_ack = 68;
    constexpr EventSymbol splitPageRankMS__kv_reduce_return = 69;
    constexpr EventSymbol splitPageRankMS__combine_flush_lane = 70;
    constexpr EventSymbol splitPageRankMS__combine_flush_ack = 71;
    constexpr EventSymbol splitPageRankMS__kv_map = 72;
    constexpr EventSymbol splitPageRankMS__sibling_rd_return = 73;
    constexpr EventSymbol splitPageRankMS__push_update = 74;
    constexpr EventSymbol splitPageRankMS__rd_nlist_return = 75;
    constexpr EventSymbol InitUpDown__init = 76;
    constexpr EventSymbol InitUpDown__terminate = 77;

} // namespace

#endif