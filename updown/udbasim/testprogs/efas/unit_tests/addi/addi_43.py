from EFA_v2 import *
def addi_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2691991604853923248, 16335]
    tran0.writeAction("movir X16 55972")
    tran0.writeAction("slorii X16 X16 12 510")
    tran0.writeAction("slorii X16 X16 12 1518")
    tran0.writeAction("slorii X16 X16 12 1426")
    tran0.writeAction("slorii X16 X16 12 592")
    tran0.writeAction("addi X16 X17 16335")
    tran0.writeAction("yieldt")
    return efa
