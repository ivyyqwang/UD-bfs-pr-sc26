from EFA_v2 import *
def fcnvt_64_b16_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13243643369034002444]
    tran0.writeAction("movir X16 47050")
    tran0.writeAction("slorii X16 X16 12 3575")
    tran0.writeAction("slorii X16 X16 12 2543")
    tran0.writeAction("slorii X16 X16 12 939")
    tran0.writeAction("slorii X16 X16 12 12")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
