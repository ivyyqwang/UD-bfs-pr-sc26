from EFA_v2 import *
def addi_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7781105439048630897, -12909]
    tran0.writeAction("movir X16 37891")
    tran0.writeAction("slorii X16 X16 12 3933")
    tran0.writeAction("slorii X16 X16 12 1097")
    tran0.writeAction("slorii X16 X16 12 2647")
    tran0.writeAction("slorii X16 X16 12 3471")
    tran0.writeAction("addi X16 X17 -12909")
    tran0.writeAction("yieldt")
    return efa
