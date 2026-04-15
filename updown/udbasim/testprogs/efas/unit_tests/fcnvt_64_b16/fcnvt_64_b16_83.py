from EFA_v2 import *
def fcnvt_64_b16_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4797750712757726751]
    tran0.writeAction("movir X16 17045")
    tran0.writeAction("slorii X16 X16 12 141")
    tran0.writeAction("slorii X16 X16 12 2698")
    tran0.writeAction("slorii X16 X16 12 3282")
    tran0.writeAction("slorii X16 X16 12 3615")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
