from EFA_v2 import *
def sladdii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8968696225975181290, 11, 719]
    tran0.writeAction("movir X16 33672")
    tran0.writeAction("slorii X16 X16 12 3236")
    tran0.writeAction("slorii X16 X16 12 3320")
    tran0.writeAction("slorii X16 X16 12 1486")
    tran0.writeAction("slorii X16 X16 12 22")
    tran0.writeAction("sladdii X16 X17 11 719")
    tran0.writeAction("yieldt")
    return efa
