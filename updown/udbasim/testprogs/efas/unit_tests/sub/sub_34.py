from EFA_v2 import *
def sub_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3989786158768072929, -6675650284376965756]
    tran0.writeAction("movir X16 51361")
    tran0.writeAction("slorii X16 X16 12 1770")
    tran0.writeAction("slorii X16 X16 12 156")
    tran0.writeAction("slorii X16 X16 12 3517")
    tran0.writeAction("slorii X16 X16 12 1823")
    tran0.writeAction("movir X17 41819")
    tran0.writeAction("slorii X17 X17 12 1334")
    tran0.writeAction("slorii X17 X17 12 3962")
    tran0.writeAction("slorii X17 X17 12 3995")
    tran0.writeAction("slorii X17 X17 12 3460")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
