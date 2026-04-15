from EFA_v2 import *
def fcnvt_64_32_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17036165126522175901]
    tran0.writeAction("movir X16 60524")
    tran0.writeAction("slorii X16 X16 12 2526")
    tran0.writeAction("slorii X16 X16 12 3021")
    tran0.writeAction("slorii X16 X16 12 1032")
    tran0.writeAction("slorii X16 X16 12 413")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
