from EFA_v2 import *
def subi_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [181412212961017082, -977]
    tran0.writeAction("movir X16 644")
    tran0.writeAction("slorii X16 X16 12 2071")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 1879")
    tran0.writeAction("slorii X16 X16 12 3322")
    tran0.writeAction("subi X16 X17 -977")
    tran0.writeAction("yieldt")
    return efa
