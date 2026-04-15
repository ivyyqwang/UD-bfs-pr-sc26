from EFA_v2 import *
def fsqrt_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10879148784509811226]
    tran0.writeAction("movir X16 38650")
    tran0.writeAction("slorii X16 X16 12 2050")
    tran0.writeAction("slorii X16 X16 12 3559")
    tran0.writeAction("slorii X16 X16 12 1351")
    tran0.writeAction("slorii X16 X16 12 2586")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
