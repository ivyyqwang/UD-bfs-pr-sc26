from EFA_v2 import *
def fcnvt_64_b16_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11541785989111281102]
    tran0.writeAction("movir X16 41004")
    tran0.writeAction("slorii X16 X16 12 2707")
    tran0.writeAction("slorii X16 X16 12 1218")
    tran0.writeAction("slorii X16 X16 12 2287")
    tran0.writeAction("slorii X16 X16 12 1486")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
