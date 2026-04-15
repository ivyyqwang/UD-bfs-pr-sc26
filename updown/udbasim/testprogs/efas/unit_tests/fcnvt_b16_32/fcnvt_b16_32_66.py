from EFA_v2 import *
def fcnvt_b16_32_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [45446]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 11")
    tran0.writeAction("slorii X16 X16 12 390")
    tran0.writeAction("fcnvt.b16.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
