from EFA_v2 import *
def sladdii_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3876198332716229327, 8, 768]
    tran0.writeAction("movir X16 51764")
    tran0.writeAction("slorii X16 X16 12 4002")
    tran0.writeAction("slorii X16 X16 12 1859")
    tran0.writeAction("slorii X16 X16 12 1997")
    tran0.writeAction("slorii X16 X16 12 3377")
    tran0.writeAction("sladdii X16 X17 8 768")
    tran0.writeAction("yieldt")
    return efa
