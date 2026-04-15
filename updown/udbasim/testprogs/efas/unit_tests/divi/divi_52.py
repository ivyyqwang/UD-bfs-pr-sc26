from EFA_v2 import *
def divi_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5002015917230193227, -16459]
    tran0.writeAction("movir X16 17770")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("slorii X16 X16 12 2451")
    tran0.writeAction("slorii X16 X16 12 1455")
    tran0.writeAction("slorii X16 X16 12 2635")
    tran0.writeAction("divi X16 X17 -16459")
    tran0.writeAction("yieldt")
    return efa
