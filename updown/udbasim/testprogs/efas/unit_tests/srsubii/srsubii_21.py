from EFA_v2 import *
def srsubii_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1051878579675654427, 9, 1833]
    tran0.writeAction("movir X16 3737")
    tran0.writeAction("slorii X16 X16 12 95")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 1678")
    tran0.writeAction("slorii X16 X16 12 2331")
    tran0.writeAction("srsubii X16 X17 9 1833")
    tran0.writeAction("yieldt")
    return efa
