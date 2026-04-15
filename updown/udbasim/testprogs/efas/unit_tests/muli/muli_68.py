from EFA_v2 import *
def muli_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3018183606158566312, -21270]
    tran0.writeAction("movir X16 54813")
    tran0.writeAction("slorii X16 X16 12 1056")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("slorii X16 X16 12 45")
    tran0.writeAction("slorii X16 X16 12 3160")
    tran0.writeAction("muli X16 X17 -21270")
    tran0.writeAction("yieldt")
    return efa
