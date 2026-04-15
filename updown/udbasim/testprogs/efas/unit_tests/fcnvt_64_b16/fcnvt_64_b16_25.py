from EFA_v2 import *
def fcnvt_64_b16_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4659766078856963631]
    tran0.writeAction("movir X16 16554")
    tran0.writeAction("slorii X16 X16 12 3336")
    tran0.writeAction("slorii X16 X16 12 3946")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("slorii X16 X16 12 1583")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
