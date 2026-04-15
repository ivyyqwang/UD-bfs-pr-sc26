from EFA_v2 import *
def fcnvt_64_b16_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3870995253829165071]
    tran0.writeAction("movir X16 13752")
    tran0.writeAction("slorii X16 X16 12 2202")
    tran0.writeAction("slorii X16 X16 12 3207")
    tran0.writeAction("slorii X16 X16 12 2910")
    tran0.writeAction("slorii X16 X16 12 15")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
