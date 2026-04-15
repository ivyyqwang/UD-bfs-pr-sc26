from EFA_v2 import *
def muli_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8556044328148585818, 12615]
    tran0.writeAction("movir X16 30397")
    tran0.writeAction("slorii X16 X16 12 719")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("slorii X16 X16 12 3244")
    tran0.writeAction("slorii X16 X16 12 3418")
    tran0.writeAction("muli X16 X17 12615")
    tran0.writeAction("yieldt")
    return efa
