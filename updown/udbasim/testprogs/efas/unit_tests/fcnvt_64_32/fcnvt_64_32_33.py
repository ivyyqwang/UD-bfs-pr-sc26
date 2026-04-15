from EFA_v2 import *
def fcnvt_64_32_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17462595548390431328]
    tran0.writeAction("movir X16 62039")
    tran0.writeAction("slorii X16 X16 12 2466")
    tran0.writeAction("slorii X16 X16 12 358")
    tran0.writeAction("slorii X16 X16 12 529")
    tran0.writeAction("slorii X16 X16 12 2656")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
