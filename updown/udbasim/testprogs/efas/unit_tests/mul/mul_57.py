from EFA_v2 import *
def mul_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8707046995966178813, -5261212381009378240]
    tran0.writeAction("movir X16 34602")
    tran0.writeAction("slorii X16 X16 12 1454")
    tran0.writeAction("slorii X16 X16 12 922")
    tran0.writeAction("slorii X16 X16 12 3292")
    tran0.writeAction("slorii X16 X16 12 2563")
    tran0.writeAction("movir X17 46844")
    tran0.writeAction("slorii X17 X17 12 1715")
    tran0.writeAction("slorii X17 X17 12 1774")
    tran0.writeAction("slorii X17 X17 12 200")
    tran0.writeAction("slorii X17 X17 12 1088")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
