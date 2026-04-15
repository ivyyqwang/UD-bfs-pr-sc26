from EFA_v2 import *
def muli_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5143614103698825959, 29545]
    tran0.writeAction("movir X16 18273")
    tran0.writeAction("slorii X16 X16 12 3228")
    tran0.writeAction("slorii X16 X16 12 1656")
    tran0.writeAction("slorii X16 X16 12 2694")
    tran0.writeAction("slorii X16 X16 12 743")
    tran0.writeAction("muli X16 X17 29545")
    tran0.writeAction("yieldt")
    return efa
