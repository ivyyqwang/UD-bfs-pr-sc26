from EFA_v2 import *
def divi_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6380330654680651268, -3806]
    tran0.writeAction("movir X16 42868")
    tran0.writeAction("slorii X16 X16 12 2097")
    tran0.writeAction("slorii X16 X16 12 754")
    tran0.writeAction("slorii X16 X16 12 918")
    tran0.writeAction("slorii X16 X16 12 2556")
    tran0.writeAction("divi X16 X17 -3806")
    tran0.writeAction("yieldt")
    return efa
