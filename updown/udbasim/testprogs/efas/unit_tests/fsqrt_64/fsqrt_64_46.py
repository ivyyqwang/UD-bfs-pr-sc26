from EFA_v2 import *
def fsqrt_64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11537592043695628987]
    tran0.writeAction("movir X16 40989")
    tran0.writeAction("slorii X16 X16 12 3117")
    tran0.writeAction("slorii X16 X16 12 1471")
    tran0.writeAction("slorii X16 X16 12 3486")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
