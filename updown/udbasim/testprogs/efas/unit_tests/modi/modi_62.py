from EFA_v2 import *
def modi_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8365015263042853196, 27198]
    tran0.writeAction("movir X16 35817")
    tran0.writeAction("slorii X16 X16 12 2031")
    tran0.writeAction("slorii X16 X16 12 33")
    tran0.writeAction("slorii X16 X16 12 2498")
    tran0.writeAction("slorii X16 X16 12 1716")
    tran0.writeAction("modi X16 X17 27198")
    tran0.writeAction("yieldt")
    return efa
