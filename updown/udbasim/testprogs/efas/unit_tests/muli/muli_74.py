from EFA_v2 import *
def muli_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7196118763005693747, -15196]
    tran0.writeAction("movir X16 25565")
    tran0.writeAction("slorii X16 X16 12 3070")
    tran0.writeAction("slorii X16 X16 12 870")
    tran0.writeAction("slorii X16 X16 12 1956")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("muli X16 X17 -15196")
    tran0.writeAction("yieldt")
    return efa
