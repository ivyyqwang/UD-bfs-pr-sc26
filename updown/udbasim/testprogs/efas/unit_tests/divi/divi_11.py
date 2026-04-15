from EFA_v2 import *
def divi_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2169047020769464449, 31491]
    tran0.writeAction("movir X16 7706")
    tran0.writeAction("slorii X16 X16 12 12")
    tran0.writeAction("slorii X16 X16 12 1526")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slorii X16 X16 12 129")
    tran0.writeAction("divi X16 X17 31491")
    tran0.writeAction("yieldt")
    return efa
