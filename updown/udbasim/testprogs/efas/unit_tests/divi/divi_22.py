from EFA_v2 import *
def divi_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6961961059457877076, 28137]
    tran0.writeAction("movir X16 40802")
    tran0.writeAction("slorii X16 X16 12 596")
    tran0.writeAction("slorii X16 X16 12 3438")
    tran0.writeAction("slorii X16 X16 12 3731")
    tran0.writeAction("slorii X16 X16 12 2988")
    tran0.writeAction("divi X16 X17 28137")
    tran0.writeAction("yieldt")
    return efa
