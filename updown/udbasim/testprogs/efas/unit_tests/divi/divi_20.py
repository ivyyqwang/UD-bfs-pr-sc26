from EFA_v2 import *
def divi_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3025669460744992637, 18335]
    tran0.writeAction("movir X16 54786")
    tran0.writeAction("slorii X16 X16 12 2714")
    tran0.writeAction("slorii X16 X16 12 2040")
    tran0.writeAction("slorii X16 X16 12 2240")
    tran0.writeAction("slorii X16 X16 12 2179")
    tran0.writeAction("divi X16 X17 18335")
    tran0.writeAction("yieldt")
    return efa
