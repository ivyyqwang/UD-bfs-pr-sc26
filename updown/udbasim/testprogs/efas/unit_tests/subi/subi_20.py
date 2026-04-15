from EFA_v2 import *
def subi_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8560887328801506642, -6682]
    tran0.writeAction("movir X16 35121")
    tran0.writeAction("slorii X16 X16 12 2533")
    tran0.writeAction("slorii X16 X16 12 1276")
    tran0.writeAction("slorii X16 X16 12 2635")
    tran0.writeAction("slorii X16 X16 12 2734")
    tran0.writeAction("subi X16 X17 -6682")
    tran0.writeAction("yieldt")
    return efa
