from EFA_v2 import *
def modi_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5992718911427930940, 15213]
    tran0.writeAction("movir X16 44245")
    tran0.writeAction("slorii X16 X16 12 2398")
    tran0.writeAction("slorii X16 X16 12 1693")
    tran0.writeAction("slorii X16 X16 12 2345")
    tran0.writeAction("slorii X16 X16 12 1220")
    tran0.writeAction("modi X16 X17 15213")
    tran0.writeAction("yieldt")
    return efa
