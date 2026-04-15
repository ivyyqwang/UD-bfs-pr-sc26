from EFA_v2 import *
def sladdii_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4976827637953058499, 5, 571]
    tran0.writeAction("movir X16 17681")
    tran0.writeAction("slorii X16 X16 12 997")
    tran0.writeAction("slorii X16 X16 12 3660")
    tran0.writeAction("slorii X16 X16 12 2205")
    tran0.writeAction("slorii X16 X16 12 1731")
    tran0.writeAction("sladdii X16 X17 5 571")
    tran0.writeAction("yieldt")
    return efa
