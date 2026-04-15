from EFA_v2 import *
def muli_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [498764574639616631, -25363]
    tran0.writeAction("movir X16 1771")
    tran0.writeAction("slorii X16 X16 12 3963")
    tran0.writeAction("slorii X16 X16 12 3313")
    tran0.writeAction("slorii X16 X16 12 3863")
    tran0.writeAction("slorii X16 X16 12 631")
    tran0.writeAction("muli X16 X17 -25363")
    tran0.writeAction("yieldt")
    return efa
