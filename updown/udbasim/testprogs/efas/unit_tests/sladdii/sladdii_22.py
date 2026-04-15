from EFA_v2 import *
def sladdii_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6469511895873870785, 11, 584]
    tran0.writeAction("movir X16 42551")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("slorii X16 X16 12 1320")
    tran0.writeAction("slorii X16 X16 12 1122")
    tran0.writeAction("slorii X16 X16 12 1087")
    tran0.writeAction("sladdii X16 X17 11 584")
    tran0.writeAction("yieldt")
    return efa
