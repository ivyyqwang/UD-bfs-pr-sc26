from EFA_v2 import *
def add_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3882714618268016456, -4045044760679916000]
    tran0.writeAction("movir X16 51741")
    tran0.writeAction("slorii X16 X16 12 3386")
    tran0.writeAction("slorii X16 X16 12 77")
    tran0.writeAction("slorii X16 X16 12 3762")
    tran0.writeAction("slorii X16 X16 12 184")
    tran0.writeAction("movir X17 51165")
    tran0.writeAction("slorii X17 X17 12 467")
    tran0.writeAction("slorii X17 X17 12 2243")
    tran0.writeAction("slorii X17 X17 12 485")
    tran0.writeAction("slorii X17 X17 12 3616")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
