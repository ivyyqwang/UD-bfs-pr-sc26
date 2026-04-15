from EFA_v2 import *
def fcnvt_64_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12912805927518239242]
    tran0.writeAction("movir X16 45875")
    tran0.writeAction("slorii X16 X16 12 2057")
    tran0.writeAction("slorii X16 X16 12 891")
    tran0.writeAction("slorii X16 X16 12 1159")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
