from EFA_v2 import *
def fcnvt_64_32_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15088804299345765834]
    tran0.writeAction("movir X16 53606")
    tran0.writeAction("slorii X16 X16 12 825")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("slorii X16 X16 12 3650")
    tran0.writeAction("slorii X16 X16 12 1482")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
