from EFA_v2 import *
def sraddii_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3314411792932925994, 15, 1477]
    tran0.writeAction("movir X16 11775")
    tran0.writeAction("slorii X16 X16 12 639")
    tran0.writeAction("slorii X16 X16 12 1813")
    tran0.writeAction("slorii X16 X16 12 543")
    tran0.writeAction("slorii X16 X16 12 554")
    tran0.writeAction("sraddii X16 X17 15 1477")
    tran0.writeAction("yieldt")
    return efa
