from EFA_v2 import *
def fcnvt_64_32_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8010623692648122811]
    tran0.writeAction("movir X16 28459")
    tran0.writeAction("slorii X16 X16 12 1852")
    tran0.writeAction("slorii X16 X16 12 3693")
    tran0.writeAction("slorii X16 X16 12 2536")
    tran0.writeAction("slorii X16 X16 12 2491")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
