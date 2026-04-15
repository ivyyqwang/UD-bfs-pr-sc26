from EFA_v2 import *
def hashl_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6361847388712150052, 669438490654741795, 1767382454927575362, 3369451047783726779]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 42934")
    tran0.writeAction("slorii X17 X17 12 728")
    tran0.writeAction("slorii X17 X17 12 424")
    tran0.writeAction("slorii X17 X17 12 2317")
    tran0.writeAction("slorii X17 X17 12 3036")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 2378")
    tran0.writeAction("slorii X17 X17 12 1324")
    tran0.writeAction("slorii X17 X17 12 682")
    tran0.writeAction("slorii X17 X17 12 1841")
    tran0.writeAction("slorii X17 X17 12 1315")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 6279")
    tran0.writeAction("slorii X17 X17 12 15")
    tran0.writeAction("slorii X17 X17 12 2704")
    tran0.writeAction("slorii X17 X17 12 884")
    tran0.writeAction("slorii X17 X17 12 2370")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 11970")
    tran0.writeAction("slorii X17 X17 12 2846")
    tran0.writeAction("slorii X17 X17 12 55")
    tran0.writeAction("slorii X17 X17 12 887")
    tran0.writeAction("slorii X17 X17 12 3771")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
