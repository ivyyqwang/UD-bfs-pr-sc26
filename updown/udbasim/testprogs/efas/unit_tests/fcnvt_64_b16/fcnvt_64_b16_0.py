from EFA_v2 import *
def fcnvt_64_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6459073917936703643]
    tran0.writeAction("movir X16 22947")
    tran0.writeAction("slorii X16 X16 12 984")
    tran0.writeAction("slorii X16 X16 12 440")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slorii X16 X16 12 2203")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
