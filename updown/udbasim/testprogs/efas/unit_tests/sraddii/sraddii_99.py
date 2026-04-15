from EFA_v2 import *
def sraddii_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1611449760087559520, 0, 88]
    tran0.writeAction("movir X16 5725")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("slorii X16 X16 12 1243")
    tran0.writeAction("slorii X16 X16 12 1668")
    tran0.writeAction("slorii X16 X16 12 3424")
    tran0.writeAction("sraddii X16 X17 0 88")
    tran0.writeAction("yieldt")
    return efa
