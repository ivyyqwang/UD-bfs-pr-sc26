from EFA_v2 import *
def mul_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1446077643609852907, -2293228626222854271]
    tran0.writeAction("movir X16 5137")
    tran0.writeAction("slorii X16 X16 12 2047")
    tran0.writeAction("slorii X16 X16 12 1160")
    tran0.writeAction("slorii X16 X16 12 4092")
    tran0.writeAction("slorii X16 X16 12 3051")
    tran0.writeAction("movir X17 57388")
    tran0.writeAction("slorii X17 X17 12 3339")
    tran0.writeAction("slorii X17 X17 12 1769")
    tran0.writeAction("slorii X17 X17 12 940")
    tran0.writeAction("slorii X17 X17 12 3969")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
