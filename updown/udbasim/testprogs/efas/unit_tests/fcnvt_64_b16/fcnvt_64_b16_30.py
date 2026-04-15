from EFA_v2 import *
def fcnvt_64_b16_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [908279842551707717]
    tran0.writeAction("movir X16 3226")
    tran0.writeAction("slorii X16 X16 12 3515")
    tran0.writeAction("slorii X16 X16 12 1115")
    tran0.writeAction("slorii X16 X16 12 3859")
    tran0.writeAction("slorii X16 X16 12 2117")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
