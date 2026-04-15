from EFA_v2 import *
def fcnvt_64_b16_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7891328254904048702]
    tran0.writeAction("movir X16 28035")
    tran0.writeAction("slorii X16 X16 12 2579")
    tran0.writeAction("slorii X16 X16 12 3295")
    tran0.writeAction("slorii X16 X16 12 2289")
    tran0.writeAction("slorii X16 X16 12 3134")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
