from EFA_v2 import *
def mul_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3195225012846731379, 2942632384892027274]
    tran0.writeAction("movir X16 11351")
    tran0.writeAction("slorii X16 X16 12 2947")
    tran0.writeAction("slorii X16 X16 12 2140")
    tran0.writeAction("slorii X16 X16 12 706")
    tran0.writeAction("slorii X16 X16 12 115")
    tran0.writeAction("movir X17 10454")
    tran0.writeAction("slorii X17 X17 12 1353")
    tran0.writeAction("slorii X17 X17 12 54")
    tran0.writeAction("slorii X17 X17 12 204")
    tran0.writeAction("slorii X17 X17 12 394")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
