from EFA_v2 import *
def subi_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5811145358994894292, -10982]
    tran0.writeAction("movir X16 20645")
    tran0.writeAction("slorii X16 X16 12 1374")
    tran0.writeAction("slorii X16 X16 12 2637")
    tran0.writeAction("slorii X16 X16 12 206")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("subi X16 X17 -10982")
    tran0.writeAction("yieldt")
    return efa
