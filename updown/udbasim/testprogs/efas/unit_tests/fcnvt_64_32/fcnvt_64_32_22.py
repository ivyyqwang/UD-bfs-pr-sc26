from EFA_v2 import *
def fcnvt_64_32_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8252980840982805389]
    tran0.writeAction("movir X16 29320")
    tran0.writeAction("slorii X16 X16 12 1957")
    tran0.writeAction("slorii X16 X16 12 2372")
    tran0.writeAction("slorii X16 X16 12 3623")
    tran0.writeAction("slorii X16 X16 12 2957")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
