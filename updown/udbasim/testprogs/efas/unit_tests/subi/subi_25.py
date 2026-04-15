from EFA_v2 import *
def subi_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1306543614201970808, -11008]
    tran0.writeAction("movir X16 60894")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("slorii X16 X16 12 343")
    tran0.writeAction("slorii X16 X16 12 3835")
    tran0.writeAction("slorii X16 X16 12 3976")
    tran0.writeAction("subi X16 X17 -11008")
    tran0.writeAction("yieldt")
    return efa
