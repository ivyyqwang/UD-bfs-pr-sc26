from EFA_v2 import *
def subi_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1453588839117391911, -28625]
    tran0.writeAction("movir X16 60371")
    tran0.writeAction("slorii X16 X16 12 3338")
    tran0.writeAction("slorii X16 X16 12 1786")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("slorii X16 X16 12 2009")
    tran0.writeAction("subi X16 X17 -28625")
    tran0.writeAction("yieldt")
    return efa
