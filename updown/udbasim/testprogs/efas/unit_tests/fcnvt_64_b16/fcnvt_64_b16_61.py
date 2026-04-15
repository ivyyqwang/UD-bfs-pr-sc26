from EFA_v2 import *
def fcnvt_64_b16_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [152739048932272764]
    tran0.writeAction("movir X16 542")
    tran0.writeAction("slorii X16 X16 12 2613")
    tran0.writeAction("slorii X16 X16 12 2834")
    tran0.writeAction("slorii X16 X16 12 3846")
    tran0.writeAction("slorii X16 X16 12 2684")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
