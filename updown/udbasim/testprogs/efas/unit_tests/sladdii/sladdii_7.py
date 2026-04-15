from EFA_v2 import *
def sladdii_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2644794663279118108, 14, 1949]
    tran0.writeAction("movir X16 56139")
    tran0.writeAction("slorii X16 X16 12 3284")
    tran0.writeAction("slorii X16 X16 12 1079")
    tran0.writeAction("slorii X16 X16 12 1635")
    tran0.writeAction("slorii X16 X16 12 2276")
    tran0.writeAction("sladdii X16 X17 14 1949")
    tran0.writeAction("yieldt")
    return efa
