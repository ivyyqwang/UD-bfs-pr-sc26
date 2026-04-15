from EFA_v2 import *
def vmul_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [396767845, -1612060462, -532777730, 174425283, -1008361973, -257785156, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2558")
    tran0.writeAction("slorii X19 X19 12 2536")
    tran0.writeAction("slorii X19 X19 8 210")
    tran0.writeAction("slorii X19 X19 12 378")
    tran0.writeAction("slorii X19 X19 12 1586")
    tran0.writeAction("slorii X19 X19 8 101")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 166")
    tran0.writeAction("slorii X17 X17 12 1412")
    tran0.writeAction("slorii X17 X17 8 195")
    tran0.writeAction("slorii X17 X17 12 3587")
    tran0.writeAction("slorii X17 X17 12 3700")
    tran0.writeAction("slorii X17 X17 8 254")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3850")
    tran0.writeAction("slorii X18 X18 12 642")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("slorii X18 X18 12 3134")
    tran0.writeAction("slorii X18 X18 12 1438")
    tran0.writeAction("slorii X18 X18 8 11")
    tran0.writeAction("vmul.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
