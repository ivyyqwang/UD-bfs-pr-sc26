from EFA_v2 import *
def divi_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4404712609961380171, 27699]
    tran0.writeAction("movir X16 15648")
    tran0.writeAction("slorii X16 X16 12 2796")
    tran0.writeAction("slorii X16 X16 12 2070")
    tran0.writeAction("slorii X16 X16 12 1768")
    tran0.writeAction("slorii X16 X16 12 2379")
    tran0.writeAction("divi X16 X17 27699")
    tran0.writeAction("yieldt")
    return efa
