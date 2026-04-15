from EFA_v2 import *
def fsqrt_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6267284711081823262]
    tran0.writeAction("movir X16 22265")
    tran0.writeAction("slorii X16 X16 12 3555")
    tran0.writeAction("slorii X16 X16 12 3390")
    tran0.writeAction("slorii X16 X16 12 1100")
    tran0.writeAction("slorii X16 X16 12 3102")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
