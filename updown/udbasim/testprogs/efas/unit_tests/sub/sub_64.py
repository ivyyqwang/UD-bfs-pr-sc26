from EFA_v2 import *
def sub_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7951912091509261261, -4218187311487105182]
    tran0.writeAction("movir X16 28250")
    tran0.writeAction("slorii X16 X16 12 3550")
    tran0.writeAction("slorii X16 X16 12 2699")
    tran0.writeAction("slorii X16 X16 12 2224")
    tran0.writeAction("slorii X16 X16 12 973")
    tran0.writeAction("movir X17 50549")
    tran0.writeAction("slorii X17 X17 12 4047")
    tran0.writeAction("slorii X17 X17 12 3382")
    tran0.writeAction("slorii X17 X17 12 3076")
    tran0.writeAction("slorii X17 X17 12 1890")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
