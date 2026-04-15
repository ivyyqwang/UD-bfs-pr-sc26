from EFA_v2 import *
def modi_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6236668489736283717, -580]
    tran0.writeAction("movir X16 22157")
    tran0.writeAction("slorii X16 X16 12 399")
    tran0.writeAction("slorii X16 X16 12 696")
    tran0.writeAction("slorii X16 X16 12 2470")
    tran0.writeAction("slorii X16 X16 12 1605")
    tran0.writeAction("modi X16 X17 -580")
    tran0.writeAction("yieldt")
    return efa
