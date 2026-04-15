from EFA_v2 import *
def fsqrt_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6968060649927274144]
    tran0.writeAction("movir X16 24755")
    tran0.writeAction("slorii X16 X16 12 2147")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slorii X16 X16 12 3744")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
