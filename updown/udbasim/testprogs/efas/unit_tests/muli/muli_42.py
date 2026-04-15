from EFA_v2 import *
def muli_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7564530620848056138, 5903]
    tran0.writeAction("movir X16 26874")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("slorii X16 X16 12 1380")
    tran0.writeAction("slorii X16 X16 12 874")
    tran0.writeAction("slorii X16 X16 12 1866")
    tran0.writeAction("muli X16 X17 5903")
    tran0.writeAction("yieldt")
    return efa
