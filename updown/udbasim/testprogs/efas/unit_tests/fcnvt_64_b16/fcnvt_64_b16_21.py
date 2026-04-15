from EFA_v2 import *
def fcnvt_64_b16_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7672541390291491710]
    tran0.writeAction("movir X16 27258")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 3676")
    tran0.writeAction("slorii X16 X16 12 3301")
    tran0.writeAction("slorii X16 X16 12 2942")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
