from EFA_v2 import *
def vgt_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [683714563, -1687199854, -703585940, -1912388752, 732731037, -86113889, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2486")
    tran0.writeAction("slorii X19 X19 12 3935")
    tran0.writeAction("slorii X19 X19 8 146")
    tran0.writeAction("slorii X19 X19 12 652")
    tran0.writeAction("slorii X19 X19 12 168")
    tran0.writeAction("slorii X19 X19 8 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2272")
    tran0.writeAction("slorii X17 X17 12 835")
    tran0.writeAction("slorii X17 X17 8 112")
    tran0.writeAction("slorii X17 X17 12 3425")
    tran0.writeAction("slorii X17 X17 12 33")
    tran0.writeAction("slorii X17 X17 8 108")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4013")
    tran0.writeAction("slorii X18 X18 12 3585")
    tran0.writeAction("slorii X18 X18 8 159")
    tran0.writeAction("slorii X18 X18 12 698")
    tran0.writeAction("slorii X18 X18 12 3222")
    tran0.writeAction("slorii X18 X18 8 157")
    tran0.writeAction("vgt.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
