from EFA_v2 import *
def slsubii_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [649742683804499583, 3, 951]
    tran0.writeAction("movir X16 2308")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("slorii X16 X16 12 1863")
    tran0.writeAction("slorii X16 X16 12 2359")
    tran0.writeAction("slorii X16 X16 12 3711")
    tran0.writeAction("slsubii X16 X17 3 951")
    tran0.writeAction("yieldt")
    return efa
