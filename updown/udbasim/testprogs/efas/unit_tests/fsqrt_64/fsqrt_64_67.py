from EFA_v2 import *
def fsqrt_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17534501951512877492]
    tran0.writeAction("movir X16 62295")
    tran0.writeAction("slorii X16 X16 12 265")
    tran0.writeAction("slorii X16 X16 12 3973")
    tran0.writeAction("slorii X16 X16 12 1305")
    tran0.writeAction("slorii X16 X16 12 2484")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
