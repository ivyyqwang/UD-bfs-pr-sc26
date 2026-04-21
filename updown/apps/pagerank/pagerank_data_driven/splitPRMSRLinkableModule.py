from linker.EFAProgram import efaProgram, EFAProgram

from libraries.UDMapShuffleReduce.linkable.LinkableKVMapShuffleCombineTPL import UDKeyValueMapShuffleReduceTemplate
from apps.pagerank_udkvmsr.pagerank_data_driven.splitPRMSRLinkableConfig import *

@efaProgram
def GenLinkableMapShuffleReduceEFA(efa: EFAProgram):

    testMSR = SplitPageRankDataDrivenMSR(efa=efa, task_name=TASK_NAME, meta_data_offset=METADATA_OFFSET, debug_flag=DEBUG_FLAG)
    testMSR.set_input_kvset(INPUT_KVSET)
    if ENABLE_REDUCE:
        testMSR.set_intermediate_kvset(INTERMEDIATE_KVSET)
        testMSR.set_output_kvset(OUTPUT_KVSET)
    
    if ENABLE_COMBINE:
        testMSR.setup_cache(cache_offset=CACHE_LM_OFFSET, num_entries=CACHE_NUM_ENTRIES, entry_size=CACHE_ENTRY_SIZE)
    if ENABLE_REDUCE:
        testMSR.set_max_thread_per_lane(max_map_th_per_lane=MAX_MAP_THREAD_PER_LANE, max_reduce_th_per_lane=MAX_REDUCE_THREAD_PER_LANE)
    else:
        testMSR.set_max_thread_per_lane(max_map_th_per_lane=MAX_MAP_THREAD_PER_LANE)

    testMSR.generate_udkvmsr_task()
    
    return efa

class SplitPageRankDataDrivenMSR(UDKeyValueMapShuffleReduceTemplate):
    
    def kv_combine_op(self, tran: EFAProgram.Transition, key: str, in_values: list, old_values: list, results: list) -> EFAProgram.Transition:
        '''
        Sum up the sibling temporary pagerank value and degree. 
        Intermediate kv pair structure:
            (long vid_op, long degree, long val_op, long active_flag)
        Parameters
            tran:       transition.
            key:        the name of the register storing the intermediate key.
            in_values:  the name of the register storing intermediate value to be combined with the current output kvpair's value corresponding with the incoming intermediate key
            old_values: the name of the register storing the current output kvpair's value corresponding with the incoming intermediate key
            results: a list of register names containing the combined values to be stored back
        '''
        for in_val, old_val, result in zip(in_values, old_values, results):
            tran.writeAction(f"fadd.64 {in_val} {old_val} {result}")
        if self.debug_flag:
            tran.writeAction(f"print '[DEBUG][NWID %ld][{self.task}] Combine Vertex %ld incoming values = " + 
                             f"[{' '.join(['%lf' for _ in range(len(in_values))])}] with cached values = " + 
                             f"[{' '.join(['%lf' for _ in range(len(old_values))])}]' {'X0'} {key} {' '.join(in_values)} {' '.join(old_values)}")
        return tran
    