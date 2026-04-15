from EFA_v2 import *
def muli_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2070444154672982320, -8386]
    tran0.writeAction("movir X16 7355")
    tran0.writeAction("slorii X16 X16 12 2847")
    tran0.writeAction("slorii X16 X16 12 3374")
    tran0.writeAction("slorii X16 X16 12 2322")
    tran0.writeAction("slorii X16 X16 12 2352")
    tran0.writeAction("muli X16 X17 -8386")
    tran0.writeAction("yieldt")
    return efa
