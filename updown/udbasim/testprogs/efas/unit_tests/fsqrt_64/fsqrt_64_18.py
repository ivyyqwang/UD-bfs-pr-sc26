from EFA_v2 import *
def fsqrt_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8911619780868100623]
    tran0.writeAction("movir X16 31660")
    tran0.writeAction("slorii X16 X16 12 1775")
    tran0.writeAction("slorii X16 X16 12 2451")
    tran0.writeAction("slorii X16 X16 12 4045")
    tran0.writeAction("slorii X16 X16 12 527")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
