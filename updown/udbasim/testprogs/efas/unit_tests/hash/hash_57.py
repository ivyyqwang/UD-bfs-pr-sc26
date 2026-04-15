from EFA_v2 import *
def hash_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1280117895769614387, -8822649966567361800]
    tran0.writeAction("movir X16 60988")
    tran0.writeAction("slorii X16 X16 12 440")
    tran0.writeAction("slorii X16 X16 12 3680")
    tran0.writeAction("slorii X16 X16 12 129")
    tran0.writeAction("slorii X16 X16 12 1997")
    tran0.writeAction("movir X17 34191")
    tran0.writeAction("slorii X17 X17 12 2665")
    tran0.writeAction("slorii X17 X17 12 2445")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
