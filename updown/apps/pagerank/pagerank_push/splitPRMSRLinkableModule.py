from linker.EFAProgram import efaProgram, EFAProgram

from libraries.UDMapShuffleReduce.linkable.LinkableKVMapShuffleCombineTPL import UDKeyValueMapShuffleReduceTemplate
from splitPRMSRLinkableConfig import *

class UDKeyValueMapShuffleReduceTemplatev2(UDKeyValueMapShuffleReduceTemplate):
    
    def kv_combine_op(self, tran: EFAProgram.Transition, key: str, in_values: list, old_values: list, results: list) -> EFAProgram.Transition:
        '''
        User defined operation used by the kv_combine to combine values to be emitted to the output kv set in the reduce task. 
        It takes an intermediate key-value pair and updates the output key value pair for that key accordingly.
        Parameters
            tran:       transition.
            key:        the name of the register storing the intermediate key.
            in_values:  the name of the register storing intermediate value to be combined with the current output kvpair's value corresponding with the incoming intermediate key
            old_values: the name of the register storing the current output kvpair's value corresponding with the incoming intermediate key
            results: a list of register names containing the combined values to be stored back
        '''
        # if DEBUG_PRINT:
        #     tran.writeAction(f"print 'combine function: key = %ld, in_vals[0] ({in_values[0]}) = %ld,  in_vals[1] ({in_values[1]}) = %ld) = %ld' {key} {in_values[0]} {in_values[1]} ")
        #     tran.writeAction(f"print 'combine function: key = %ld, old_vals[0] ({old_values[0]}) = %ld,  old_vals[1] ({old_values[1]}) = %ld) = %ld' {key} {old_values[0]} {old_values[1]}")
        # user defined combine function
        
        for in_val, old_val, result in zip(in_values, old_values, results):
            if DEBUG_FLAG:
                tran.writeAction(f"print 'combine function: key = %ld {in_val} = %lf,  {old_val} = %lf' {key} {in_val} {old_val}")
            tran.writeAction(f"fadd.64 {in_val} {old_val} {result}")
        return tran

@efaProgram
def GenLinkableMapShuffleReduceEFA(efa: EFAProgram):

    testMSR = UDKeyValueMapShuffleReduceTemplatev2(efa=efa, task_name=TASK_NAME, meta_data_offset=METADATA_OFFSET, debug_flag=DEBUG_FLAG)
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