from EFA_v2 import *
def fcnvt_64_32_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6692612822273688573]
    tran0.writeAction("movir X16 23776")
    tran0.writeAction("slorii X16 X16 12 3838")
    tran0.writeAction("slorii X16 X16 12 1826")
    tran0.writeAction("slorii X16 X16 12 3472")
    tran0.writeAction("slorii X16 X16 12 1021")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
