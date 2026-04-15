from EFA_v2 import *
def fcnvt_64_32_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15100180844894884129]
    tran0.writeAction("movir X16 53646")
    tran0.writeAction("slorii X16 X16 12 2535")
    tran0.writeAction("slorii X16 X16 12 2408")
    tran0.writeAction("slorii X16 X16 12 481")
    tran0.writeAction("slorii X16 X16 12 289")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
