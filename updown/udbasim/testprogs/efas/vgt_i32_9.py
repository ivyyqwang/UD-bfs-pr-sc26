from EFA_v2 import *
def vgt_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [468450945, -1087639910, -1169243633, -508934344, 2009947411, -642022257, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3058")
    tran0.writeAction("slorii X19 X19 12 3054")
    tran0.writeAction("slorii X19 X19 8 154")
    tran0.writeAction("slorii X19 X19 12 446")
    tran0.writeAction("slorii X19 X19 12 3070")
    tran0.writeAction("slorii X19 X19 8 129")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3610")
    tran0.writeAction("slorii X17 X17 12 2631")
    tran0.writeAction("slorii X17 X17 8 56")
    tran0.writeAction("slorii X17 X17 12 2980")
    tran0.writeAction("slorii X17 X17 12 3778")
    tran0.writeAction("slorii X17 X17 8 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3483")
    tran0.writeAction("slorii X18 X18 12 2948")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("slorii X18 X18 12 1916")
    tran0.writeAction("slorii X18 X18 12 3421")
    tran0.writeAction("slorii X18 X18 8 19")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
