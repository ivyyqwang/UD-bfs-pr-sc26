from EFA_v2 import *
def fcnvt_64_b16_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13930222269466324493]
    tran0.writeAction("movir X16 49490")
    tran0.writeAction("slorii X16 X16 12 373")
    tran0.writeAction("slorii X16 X16 12 2365")
    tran0.writeAction("slorii X16 X16 12 3178")
    tran0.writeAction("slorii X16 X16 12 3597")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
