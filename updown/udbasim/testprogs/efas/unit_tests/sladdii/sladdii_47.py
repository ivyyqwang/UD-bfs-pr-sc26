from EFA_v2 import *
def sladdii_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2323060862878219602, 4, 979]
    tran0.writeAction("movir X16 57282")
    tran0.writeAction("slorii X16 X16 12 3399")
    tran0.writeAction("slorii X16 X16 12 1036")
    tran0.writeAction("slorii X16 X16 12 2176")
    tran0.writeAction("slorii X16 X16 12 686")
    tran0.writeAction("sladdii X16 X17 4 979")
    tran0.writeAction("yieldt")
    return efa
