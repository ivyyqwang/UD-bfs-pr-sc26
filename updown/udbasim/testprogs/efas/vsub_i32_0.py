from EFA_v2 import *
def vsub_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1604023720, -967998004, 1855881651, -857807051, -1897837029, 2007134524, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3172")
    tran0.writeAction("slorii X19 X19 12 3461")
    tran0.writeAction("slorii X19 X19 8 204")
    tran0.writeAction("slorii X19 X19 12 1529")
    tran0.writeAction("slorii X19 X19 12 2933")
    tran0.writeAction("slorii X19 X19 8 168")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3277")
    tran0.writeAction("slorii X17 X17 12 3815")
    tran0.writeAction("slorii X17 X17 8 53")
    tran0.writeAction("slorii X17 X17 12 1769")
    tran0.writeAction("slorii X17 X17 12 3713")
    tran0.writeAction("slorii X17 X17 8 179")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1914")
    tran0.writeAction("slorii X18 X18 12 625")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("slorii X18 X18 12 2286")
    tran0.writeAction("slorii X18 X18 12 334")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
