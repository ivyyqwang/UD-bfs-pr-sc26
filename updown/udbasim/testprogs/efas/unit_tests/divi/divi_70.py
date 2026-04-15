from EFA_v2 import *
def divi_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3621001434580741219, 10278]
    tran0.writeAction("movir X16 12864")
    tran0.writeAction("slorii X16 X16 12 1561")
    tran0.writeAction("slorii X16 X16 12 3759")
    tran0.writeAction("slorii X16 X16 12 1494")
    tran0.writeAction("slorii X16 X16 12 3171")
    tran0.writeAction("divi X16 X17 10278")
    tran0.writeAction("yieldt")
    return efa
