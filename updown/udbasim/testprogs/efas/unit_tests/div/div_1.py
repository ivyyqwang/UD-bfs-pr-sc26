from EFA_v2 import *
def div_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7289898950074773392, -2330915421942168415]
    tran0.writeAction("movir X16 39637")
    tran0.writeAction("slorii X16 X16 12 312")
    tran0.writeAction("slorii X16 X16 12 1864")
    tran0.writeAction("slorii X16 X16 12 1229")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("movir X17 57254")
    tran0.writeAction("slorii X17 X17 12 3788")
    tran0.writeAction("slorii X17 X17 12 1537")
    tran0.writeAction("slorii X17 X17 12 2692")
    tran0.writeAction("slorii X17 X17 12 1185")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
