from EFA_v2 import *
def modi_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7397176645642726504, -18440]
    tran0.writeAction("movir X16 39255")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 2143")
    tran0.writeAction("slorii X16 X16 12 2661")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("modi X16 X17 -18440")
    tran0.writeAction("yieldt")
    return efa
