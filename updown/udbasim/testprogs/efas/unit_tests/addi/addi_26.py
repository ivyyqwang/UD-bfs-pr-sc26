from EFA_v2 import *
def addi_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8645123048619027319, -20932]
    tran0.writeAction("movir X16 30713")
    tran0.writeAction("slorii X16 X16 12 2649")
    tran0.writeAction("slorii X16 X16 12 3040")
    tran0.writeAction("slorii X16 X16 12 1962")
    tran0.writeAction("slorii X16 X16 12 2935")
    tran0.writeAction("addi X16 X17 -20932")
    tran0.writeAction("yieldt")
    return efa
