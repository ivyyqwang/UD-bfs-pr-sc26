from EFA_v2 import *
def vmadd_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2091636057, -897258954, -396706989, -1407434160, -1870358870, -781980520, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3240")
    tran0.writeAction("slorii X19 X19 12 1258")
    tran0.writeAction("slorii X19 X19 8 54")
    tran0.writeAction("slorii X19 X19 12 2101")
    tran0.writeAction("slorii X19 X19 12 1066")
    tran0.writeAction("slorii X19 X19 8 167")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2753")
    tran0.writeAction("slorii X17 X17 12 3138")
    tran0.writeAction("slorii X17 X17 8 80")
    tran0.writeAction("slorii X17 X17 12 3717")
    tran0.writeAction("slorii X17 X17 12 2747")
    tran0.writeAction("slorii X17 X17 8 83")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3350")
    tran0.writeAction("slorii X18 X18 12 1004")
    tran0.writeAction("slorii X18 X18 8 152")
    tran0.writeAction("slorii X18 X18 12 2312")
    tran0.writeAction("slorii X18 X18 12 1174")
    tran0.writeAction("slorii X18 X18 8 170")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
