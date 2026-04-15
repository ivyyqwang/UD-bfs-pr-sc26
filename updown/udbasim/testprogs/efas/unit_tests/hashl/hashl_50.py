from EFA_v2 import *
def hashl_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-597100721806802241, 2800214248401019118, -1137579415740068590]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63414")
    tran0.writeAction("slorii X17 X17 12 2752")
    tran0.writeAction("slorii X17 X17 12 3741")
    tran0.writeAction("slorii X17 X17 12 2360")
    tran0.writeAction("slorii X17 X17 12 703")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 9948")
    tran0.writeAction("slorii X17 X17 12 1472")
    tran0.writeAction("slorii X17 X17 12 1490")
    tran0.writeAction("slorii X17 X17 12 3810")
    tran0.writeAction("slorii X17 X17 12 238")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 61494")
    tran0.writeAction("slorii X17 X17 12 2072")
    tran0.writeAction("slorii X17 X17 12 3181")
    tran0.writeAction("slorii X17 X17 12 68")
    tran0.writeAction("slorii X17 X17 12 3346")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
