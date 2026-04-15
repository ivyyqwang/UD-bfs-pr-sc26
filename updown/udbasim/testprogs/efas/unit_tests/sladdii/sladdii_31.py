from EFA_v2 import *
def sladdii_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5197211137535485030, 9, 1960]
    tran0.writeAction("movir X16 47071")
    tran0.writeAction("slorii X16 X16 12 3264")
    tran0.writeAction("slorii X16 X16 12 420")
    tran0.writeAction("slorii X16 X16 12 2021")
    tran0.writeAction("slorii X16 X16 12 2970")
    tran0.writeAction("sladdii X16 X17 9 1960")
    tran0.writeAction("yieldt")
    return efa
