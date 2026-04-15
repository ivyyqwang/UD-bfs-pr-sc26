from EFA_v2 import *
def sub_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6573400591269754459, 6922066684486691505]
    tran0.writeAction("movir X16 23353")
    tran0.writeAction("slorii X16 X16 12 1680")
    tran0.writeAction("slorii X16 X16 12 680")
    tran0.writeAction("slorii X16 X16 12 3999")
    tran0.writeAction("slorii X16 X16 12 1627")
    tran0.writeAction("movir X17 24592")
    tran0.writeAction("slorii X17 X17 12 495")
    tran0.writeAction("slorii X17 X17 12 2448")
    tran0.writeAction("slorii X17 X17 12 1618")
    tran0.writeAction("slorii X17 X17 12 2737")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
