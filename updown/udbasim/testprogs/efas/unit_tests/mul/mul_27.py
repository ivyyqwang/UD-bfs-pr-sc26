from EFA_v2 import *
def mul_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2538664680367252357, -3129501920691596168]
    tran0.writeAction("movir X16 56516")
    tran0.writeAction("slorii X16 X16 12 3486")
    tran0.writeAction("slorii X16 X16 12 3186")
    tran0.writeAction("slorii X16 X16 12 3601")
    tran0.writeAction("slorii X16 X16 12 3195")
    tran0.writeAction("movir X17 54417")
    tran0.writeAction("slorii X17 X17 12 3177")
    tran0.writeAction("slorii X17 X17 12 1405")
    tran0.writeAction("slorii X17 X17 12 1125")
    tran0.writeAction("slorii X17 X17 12 1144")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
