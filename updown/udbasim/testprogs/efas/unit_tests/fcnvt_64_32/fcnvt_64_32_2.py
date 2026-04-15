from EFA_v2 import *
def fcnvt_64_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7681377799220898648]
    tran0.writeAction("movir X16 27289")
    tran0.writeAction("slorii X16 X16 12 3014")
    tran0.writeAction("slorii X16 X16 12 2340")
    tran0.writeAction("slorii X16 X16 12 546")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
