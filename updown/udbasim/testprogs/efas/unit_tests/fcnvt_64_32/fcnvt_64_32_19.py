from EFA_v2 import *
def fcnvt_64_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15160089398029464473]
    tran0.writeAction("movir X16 53859")
    tran0.writeAction("slorii X16 X16 12 1871")
    tran0.writeAction("slorii X16 X16 12 3172")
    tran0.writeAction("slorii X16 X16 12 2915")
    tran0.writeAction("slorii X16 X16 12 921")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
