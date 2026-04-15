from EFA_v2 import *
def add_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8157746463672067863, -9002084421410126060]
    tran0.writeAction("movir X16 36553")
    tran0.writeAction("slorii X16 X16 12 3533")
    tran0.writeAction("slorii X16 X16 12 25")
    tran0.writeAction("slorii X16 X16 12 521")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("movir X17 33554")
    tran0.writeAction("slorii X17 X17 12 702")
    tran0.writeAction("slorii X17 X17 12 2543")
    tran0.writeAction("slorii X17 X17 12 3160")
    tran0.writeAction("slorii X17 X17 12 1812")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
