'''
Example configuration file for generating UDKVMSR linkable module.
'''

from libraries.UDMapShuffleReduce.utils.OneDimArrayKeyValueSet import OneDimKeyValueSet, MaskedOneDimKeyValueSet
from libraries.UDMapShuffleReduce.utils.IntermediateKeyValueSet import IntermediateKeyValueSet
from libraries.LMStaticMaps.LMStaticMap import *
from linker.EFAProgram import EFAProgram

NUM_NODES = 4

class OneDimKeyValueSetv2(OneDimKeyValueSet):
    def get_next_pair(self, tran: EFAProgram.Transition, cont_evw: str, map_ev_word: str, map_ev_label: str, iterator: list, regs: list, reach_end_label: str) -> EFAProgram.Transition:
        tran.writeAction(f"bge {iterator[0]} {iterator[1]} {reach_end_label}")
        tran.writeAction(f"movir {regs[0]} {self.element_bsize*2048}")
        tran.writeAction(f"muli {regs[0]} {regs[0]} {NUM_NODES}")
        tran.writeAction(f"add {iterator[0]} {regs[0]} {regs[0]}")
        tran.writeAction(f"sendr_wcont {cont_evw} {cont_evw} {regs[0]} {iterator[1]}")
        tran.writeAction(f"send_dmlm_ld {iterator[0]} {map_ev_word} {self.element_size}")
        return tran
    
    def get_pair(self, tran: EFAProgram.Transition, cont_evw: str, key: str, regs: list) -> EFAProgram.Transition:
        tran.writeAction(f"move {self.meta_data_offset}(X7) {regs[0]} 0 {WORD_SIZE}")
        if self.power_of_two:
            tran.writeAction(f"lshift {key} {regs[1]} {self.log2_element_size + LOG2_WORD_SIZE}")
        else:
            tran.writeAction(f"muli {key} {regs[1]} {self.element_bsize + 8}")
        tran.writeAction(f"add {regs[1]} {regs[0]} {regs[0]}")
        tran.writeAction(f"send_dmlm_ld {regs[0]} {cont_evw} {self.element_size}")
        return tran

    def put_pair(self, tran: EFAProgram.Transition, cont_evw: str,  key: str, values: list, buffer_addr: str, regs: list) -> EFAProgram.Transition:
        tran.writeAction(f"movlr {self.meta_data_offset}(X7) {regs[0]} 0 {WORD_SIZE}")
        if self.power_of_two:
            tran.writeAction(f"lshift {key} {regs[1]} {self.log2_element_size + LOG2_WORD_SIZE}")
        else:
            tran.writeAction(f"muli {key} {regs[1]} {self.element_bsize + 8}")
        tran.writeAction(f"add {regs[1]} {regs[0]} {regs[0]}")
        for val in values:
            tran.writeAction(f"movrl {val} 0({buffer_addr}) 1 {WORD_SIZE}")
        tran.writeAction(f"subi {buffer_addr} {buffer_addr} {self.element_bsize}")
        tran.writeAction(f"send_dmlm {regs[0]} {cont_evw} {buffer_addr} {self.element_size}")
        return tran
    
    def flush_pair(self, tran: EFAProgram.Transition, cont_evw: str, key: str, value_addr: str, buffer_addr: str, num_acks: str, regs: list) -> EFAProgram.Transition:
        tran.writeAction(f"movlr {self.meta_data_offset}(X7) {regs[0]} 0 {WORD_SIZE}")
        if self.power_of_two:
            tran.writeAction(f"lshift {key} {regs[1]} {self.log2_element_size + LOG2_WORD_SIZE}")
        else:
            tran.writeAction(f"muli {key} {regs[1]} {self.element_bsize + 8}")
        tran.writeAction(f"add {regs[1]} {regs[0]} {regs[0]}")
        tran.writeAction(f"send_dmlm {regs[0]} {cont_evw} {value_addr} {self.element_size}")
        tran.writeAction(f"addi {value_addr} {value_addr} {self.element_bsize}")
        tran.writeAction(f"addi {num_acks} {num_acks} {1}")
        return tran


'''
UDKVMSR program configuration. The following parameters are required:
    task_name:      unique identifier for each UDKVMSR program.
    metadata_offset:   offset of the metadata in bytes. Reserve 32 words on each lane, starting from the offset.
    debug_flag:     enable debug print (optional), default is False
'''
TASK_NAME       = "splitPageRankMS"
METADATA_OFFSET = UDKVMSR_0_OFFSET
DEBUG_FLAG      = False
# MAX_MAP_THREAD_PER_LANE     = 24
MAX_MAP_THREAD_PER_LANE     = 8
MAX_REDUCE_THREAD_PER_LANE  = 220

# The usage of kv_combine is optional. If not enabled, set ENABLE_COMBINE to False.
ENABLE_COMBINE      = True
'''
Cache configuration. Required if kv_combine is used in reduce.
    cache_offset:   scratchpad bank offset (Bytes) for the cache. 
    num_entries:    number of entries per lane
    entry_size:     size of each entry (in words)
'''
CACHE_LM_OFFSET     = HEAP_OFFSET
CACHE_NUM_ENTRIES   = 2048
CACHE_ENTRY_SIZE    = 2

'''
Define the input, intermediate and output key value set. 
Available key value set types:
    OneDimKeyValueSet:          One dimensional array in DRAM, key is implicitly the index of the array, value is the element in the array.
                                Init parameters: 
                                    name         - name of the key value set
                                    element_size - size of each element in the array (in words)
    IntermediateKeyValueSet:    Dummy set for intermediate key-value pair emitted by map task.
                                Init parameters:
                                    name        - name of the key value set
                                    key_size    - size of the key (in words)
                                    value_size  - size of the value (in words)
    SHTKeyValueSet:             Multi-word scalable hash table. 
                                Init parameters:
                                    name        - name of the key value set
                                    value_size  - size of the value (in words)
    SingleWordSHTKeyValueSet:   Single-word scalable hash table.
                                Init parameters:
                                    name        - name of the key value set
'''
# Input array configuration
INPUT_ARRAY_ELEMENT_SIZE = 8
INPUT_KVSET = OneDimKeyValueSet(name=f"{TASK_NAME}_input", element_size=INPUT_ARRAY_ELEMENT_SIZE, bypass_gen_partition=True)

# Reduce is optional. If not enabled, set ENABLE_REDUCE to False.
ENABLE_REDUCE   = True    
# Intermediate key value pair configuration
INTERMEDIATE_KEY_SIZE   = 1
INTERMEDIATE_VALUE_SIZE = 1
INTERMEDIATE_KVSET = IntermediateKeyValueSet(name=f"{TASK_NAME}_intermediate", key_size=INTERMEDIATE_KEY_SIZE, value_size=INTERMEDIATE_VALUE_SIZE)

# Output array configuration
OUTPUT_ARRAY_ELEMENT_SIZE = 1
OUTPUT_KVSET = MaskedOneDimKeyValueSet(name=f"{TASK_NAME}_output", element_size=OUTPUT_ARRAY_ELEMENT_SIZE, mask='1')
