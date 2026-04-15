from EFA_v2 import *
def divi_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-748974188181094514, 10038]
    tran0.writeAction("movir X16 62875")
    tran0.writeAction("slorii X16 X16 12 447")
    tran0.writeAction("slorii X16 X16 12 431")
    tran0.writeAction("slorii X16 X16 12 2167")
    tran0.writeAction("slorii X16 X16 12 3982")
    tran0.writeAction("divi X16 X17 10038")
    tran0.writeAction("yieldt")
    return efa
