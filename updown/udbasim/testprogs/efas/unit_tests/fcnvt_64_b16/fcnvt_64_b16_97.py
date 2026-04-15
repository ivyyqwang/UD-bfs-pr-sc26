from EFA_v2 import *
def fcnvt_64_b16_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5189547652009063919]
    tran0.writeAction("movir X16 18436")
    tran0.writeAction("slorii X16 X16 12 4001")
    tran0.writeAction("slorii X16 X16 12 2070")
    tran0.writeAction("slorii X16 X16 12 3943")
    tran0.writeAction("slorii X16 X16 12 1519")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
