from EFA_v2 import *
def sub_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [568205745517724233, -3639257801696190477]
    tran0.writeAction("movir X16 2018")
    tran0.writeAction("slorii X16 X16 12 2753")
    tran0.writeAction("slorii X16 X16 12 3444")
    tran0.writeAction("slorii X16 X16 12 3768")
    tran0.writeAction("slorii X16 X16 12 585")
    tran0.writeAction("movir X17 52606")
    tran0.writeAction("slorii X17 X17 12 3108")
    tran0.writeAction("slorii X17 X17 12 3995")
    tran0.writeAction("slorii X17 X17 12 3397")
    tran0.writeAction("slorii X17 X17 12 4083")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
