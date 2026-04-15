from EFA_v2 import *
def modi_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5427833804435734272, 17318]
    tran0.writeAction("movir X16 46252")
    tran0.writeAction("slorii X16 X16 12 1886")
    tran0.writeAction("slorii X16 X16 12 2474")
    tran0.writeAction("slorii X16 X16 12 3076")
    tran0.writeAction("slorii X16 X16 12 256")
    tran0.writeAction("modi X16 X17 17318")
    tran0.writeAction("yieldt")
    return efa
