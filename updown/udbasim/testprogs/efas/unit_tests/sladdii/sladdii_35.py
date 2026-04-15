from EFA_v2 import *
def sladdii_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-803587344911888170, 6, 784]
    tran0.writeAction("movir X16 62681")
    tran0.writeAction("slorii X16 X16 12 345")
    tran0.writeAction("slorii X16 X16 12 320")
    tran0.writeAction("slorii X16 X16 12 2161")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("sladdii X16 X17 6 784")
    tran0.writeAction("yieldt")
    return efa
