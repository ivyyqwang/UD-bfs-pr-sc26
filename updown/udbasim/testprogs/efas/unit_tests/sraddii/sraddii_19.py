from EFA_v2 import *
def sraddii_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6822498289121465979, 0, 1160]
    tran0.writeAction("movir X16 24238")
    tran0.writeAction("slorii X16 X16 12 1568")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 3257")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("sraddii X16 X17 0 1160")
    tran0.writeAction("yieldt")
    return efa
