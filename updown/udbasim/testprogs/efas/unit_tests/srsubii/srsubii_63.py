from EFA_v2 import *
def srsubii_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2023175071408295968, 14, 1993]
    tran0.writeAction("movir X16 58348")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("slorii X16 X16 12 3558")
    tran0.writeAction("slorii X16 X16 12 1158")
    tran0.writeAction("slorii X16 X16 12 4064")
    tran0.writeAction("srsubii X16 X17 14 1993")
    tran0.writeAction("yieldt")
    return efa
