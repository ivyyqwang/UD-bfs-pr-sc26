from EFA_v2 import *
def fcnvt_i64_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1933578150538852236]
    tran0.writeAction("movir X16 58666")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("slorii X16 X16 12 2727")
    tran0.writeAction("slorii X16 X16 12 2764")
    tran0.writeAction("slorii X16 X16 12 2164")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
