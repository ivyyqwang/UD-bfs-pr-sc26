from EFA_v2 import *
def addi_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1094918263863582413, -23660]
    tran0.writeAction("movir X16 61646")
    tran0.writeAction("slorii X16 X16 12 282")
    tran0.writeAction("slorii X16 X16 12 992")
    tran0.writeAction("slorii X16 X16 12 1326")
    tran0.writeAction("slorii X16 X16 12 307")
    tran0.writeAction("addi X16 X17 -23660")
    tran0.writeAction("yieldt")
    return efa
