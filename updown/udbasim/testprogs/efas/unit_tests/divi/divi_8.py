from EFA_v2 import *
def divi_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7297640027460913783, -5186]
    tran0.writeAction("movir X16 39609")
    tran0.writeAction("slorii X16 X16 12 2352")
    tran0.writeAction("slorii X16 X16 12 3904")
    tran0.writeAction("slorii X16 X16 12 2131")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("divi X16 X17 -5186")
    tran0.writeAction("yieldt")
    return efa
