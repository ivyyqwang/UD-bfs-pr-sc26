from EFA_v2 import *
def fcnvt_64_b16_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7716937948767952360]
    tran0.writeAction("movir X16 27416")
    tran0.writeAction("slorii X16 X16 12 290")
    tran0.writeAction("slorii X16 X16 12 3494")
    tran0.writeAction("slorii X16 X16 12 185")
    tran0.writeAction("slorii X16 X16 12 3560")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
