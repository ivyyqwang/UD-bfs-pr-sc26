from EFA_v2 import *
def mul_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5271458731574652677, 1582366947336877091]
    tran0.writeAction("movir X16 46808")
    tran0.writeAction("slorii X16 X16 12 67")
    tran0.writeAction("slorii X16 X16 12 1672")
    tran0.writeAction("slorii X16 X16 12 1481")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("movir X17 5621")
    tran0.writeAction("slorii X17 X17 12 2853")
    tran0.writeAction("slorii X17 X17 12 2776")
    tran0.writeAction("slorii X17 X17 12 1367")
    tran0.writeAction("slorii X17 X17 12 1059")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
