from EFA_v2 import *
def sladdii_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3246191862655354119, 9, 1600]
    tran0.writeAction("movir X16 54003")
    tran0.writeAction("slorii X16 X16 12 859")
    tran0.writeAction("slorii X16 X16 12 817")
    tran0.writeAction("slorii X16 X16 12 2719")
    tran0.writeAction("slorii X16 X16 12 2809")
    tran0.writeAction("sladdii X16 X17 9 1600")
    tran0.writeAction("yieldt")
    return efa
