from EFA_v2 import *
def sladdii_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-843003956840998234, 14, 1484]
    tran0.writeAction("movir X16 62541")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("slorii X16 X16 12 3616")
    tran0.writeAction("slorii X16 X16 12 997")
    tran0.writeAction("slorii X16 X16 12 2726")
    tran0.writeAction("sladdii X16 X17 14 1484")
    tran0.writeAction("yieldt")
    return efa
