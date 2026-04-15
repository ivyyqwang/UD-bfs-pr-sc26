from EFA_v2 import *
def vfill_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [589410534, -1534538851, 1512]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2632")
    tran0.writeAction("slorii X18 X18 12 2251")
    tran0.writeAction("slorii X18 X18 8 157")
    tran0.writeAction("slorii X18 X18 12 562")
    tran0.writeAction("slorii X18 X18 12 432")
    tran0.writeAction("slorii X18 X18 8 230")
    tran0.writeAction("vfill.i32 X18 1512 ")
    tran0.writeAction("yieldt")
    return efa
