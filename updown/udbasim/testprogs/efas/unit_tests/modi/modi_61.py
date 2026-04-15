from EFA_v2 import *
def modi_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5904946630956556926, -14939]
    tran0.writeAction("movir X16 44557")
    tran0.writeAction("slorii X16 X16 12 1701")
    tran0.writeAction("slorii X16 X16 12 812")
    tran0.writeAction("slorii X16 X16 12 797")
    tran0.writeAction("slorii X16 X16 12 3458")
    tran0.writeAction("modi X16 X17 -14939")
    tran0.writeAction("yieldt")
    return efa
