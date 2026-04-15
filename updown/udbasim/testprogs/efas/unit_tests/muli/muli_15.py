from EFA_v2 import *
def muli_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [27203786069994162, 14030]
    tran0.writeAction("movir X16 96")
    tran0.writeAction("slorii X16 X16 12 2651")
    tran0.writeAction("slorii X16 X16 12 773")
    tran0.writeAction("slorii X16 X16 12 1014")
    tran0.writeAction("slorii X16 X16 12 2738")
    tran0.writeAction("muli X16 X17 14030")
    tran0.writeAction("yieldt")
    return efa
