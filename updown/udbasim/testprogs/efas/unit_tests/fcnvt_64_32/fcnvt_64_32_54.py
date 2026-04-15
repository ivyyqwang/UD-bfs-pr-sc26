from EFA_v2 import *
def fcnvt_64_32_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12224288441756103764]
    tran0.writeAction("movir X16 43429")
    tran0.writeAction("slorii X16 X16 12 1625")
    tran0.writeAction("slorii X16 X16 12 538")
    tran0.writeAction("slorii X16 X16 12 3219")
    tran0.writeAction("slorii X16 X16 12 1108")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
