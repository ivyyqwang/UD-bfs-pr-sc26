from EFA_v2 import *
def fsqrt_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9568548941478157360]
    tran0.writeAction("movir X16 33994")
    tran0.writeAction("slorii X16 X16 12 1289")
    tran0.writeAction("slorii X16 X16 12 224")
    tran0.writeAction("slorii X16 X16 12 3053")
    tran0.writeAction("slorii X16 X16 12 3120")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
