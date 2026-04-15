from EFA_v2 import *
def fcnvt_64_b16_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5130584171248546263]
    tran0.writeAction("movir X16 18227")
    tran0.writeAction("slorii X16 X16 12 2033")
    tran0.writeAction("slorii X16 X16 12 3817")
    tran0.writeAction("slorii X16 X16 12 2095")
    tran0.writeAction("slorii X16 X16 12 471")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
