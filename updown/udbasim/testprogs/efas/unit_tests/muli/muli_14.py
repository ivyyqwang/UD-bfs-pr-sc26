from EFA_v2 import *
def muli_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [765216119755734993, 11156]
    tran0.writeAction("movir X16 2718")
    tran0.writeAction("slorii X16 X16 12 2432")
    tran0.writeAction("slorii X16 X16 12 434")
    tran0.writeAction("slorii X16 X16 12 1815")
    tran0.writeAction("slorii X16 X16 12 4049")
    tran0.writeAction("muli X16 X17 11156")
    tran0.writeAction("yieldt")
    return efa
