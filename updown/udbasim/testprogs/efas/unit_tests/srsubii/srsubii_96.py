from EFA_v2 import *
def srsubii_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7087846671909697684, 6, 1346]
    tran0.writeAction("movir X16 40354")
    tran0.writeAction("slorii X16 X16 12 3728")
    tran0.writeAction("slorii X16 X16 12 322")
    tran0.writeAction("slorii X16 X16 12 1588")
    tran0.writeAction("slorii X16 X16 12 1900")
    tran0.writeAction("srsubii X16 X17 6 1346")
    tran0.writeAction("yieldt")
    return efa
