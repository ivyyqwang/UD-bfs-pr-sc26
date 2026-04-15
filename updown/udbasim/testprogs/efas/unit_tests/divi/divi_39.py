from EFA_v2 import *
def divi_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1723659843799640329, 15123]
    tran0.writeAction("movir X16 6123")
    tran0.writeAction("slorii X16 X16 12 2743")
    tran0.writeAction("slorii X16 X16 12 3807")
    tran0.writeAction("slorii X16 X16 12 1158")
    tran0.writeAction("slorii X16 X16 12 2313")
    tran0.writeAction("divi X16 X17 15123")
    tran0.writeAction("yieldt")
    return efa
