from EFA_v2 import *
def addi_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9201901131951896985, 27564]
    tran0.writeAction("movir X16 32844")
    tran0.writeAction("slorii X16 X16 12 1146")
    tran0.writeAction("slorii X16 X16 12 3227")
    tran0.writeAction("slorii X16 X16 12 3040")
    tran0.writeAction("slorii X16 X16 12 1639")
    tran0.writeAction("addi X16 X17 27564")
    tran0.writeAction("yieldt")
    return efa
