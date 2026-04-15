from EFA_v2 import *
def fcnvt_b16_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [50735]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 12")
    tran0.writeAction("slorii X16 X16 12 1583")
    tran0.writeAction("fcnvt.b16.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
