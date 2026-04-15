from EFA_v2 import *
def fcnvt_64_b16_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9988781297910016674]
    tran0.writeAction("movir X16 35487")
    tran0.writeAction("slorii X16 X16 12 1146")
    tran0.writeAction("slorii X16 X16 12 2792")
    tran0.writeAction("slorii X16 X16 12 4062")
    tran0.writeAction("slorii X16 X16 12 2722")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
