from EFA_v2 import *
def divi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3124787585429901530, 32432]
    tran0.writeAction("movir X16 54434")
    tran0.writeAction("slorii X16 X16 12 2147")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("slorii X16 X16 12 3686")
    tran0.writeAction("slorii X16 X16 12 3878")
    tran0.writeAction("divi X16 X17 32432")
    tran0.writeAction("yieldt")
    return efa
