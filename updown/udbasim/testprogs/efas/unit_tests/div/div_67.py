from EFA_v2 import *
def div_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [691588466882975052, -6533709863847489462]
    tran0.writeAction("movir X16 2457")
    tran0.writeAction("slorii X16 X16 12 64")
    tran0.writeAction("slorii X16 X16 12 3043")
    tran0.writeAction("slorii X16 X16 12 1297")
    tran0.writeAction("slorii X16 X16 12 1356")
    tran0.writeAction("movir X17 42323")
    tran0.writeAction("slorii X17 X17 12 2455")
    tran0.writeAction("slorii X17 X17 12 3827")
    tran0.writeAction("slorii X17 X17 12 3705")
    tran0.writeAction("slorii X17 X17 12 74")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
