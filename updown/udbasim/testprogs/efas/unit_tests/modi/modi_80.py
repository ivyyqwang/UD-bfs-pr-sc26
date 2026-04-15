from EFA_v2 import *
def modi_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5808156492456168249, 9437]
    tran0.writeAction("movir X16 44901")
    tran0.writeAction("slorii X16 X16 12 1159")
    tran0.writeAction("slorii X16 X16 12 363")
    tran0.writeAction("slorii X16 X16 12 1111")
    tran0.writeAction("slorii X16 X16 12 1223")
    tran0.writeAction("modi X16 X17 9437")
    tran0.writeAction("yieldt")
    return efa
