from EFA_v2 import *
def fsqrt_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8064385736052993061]
    tran0.writeAction("movir X16 28650")
    tran0.writeAction("slorii X16 X16 12 1857")
    tran0.writeAction("slorii X16 X16 12 2457")
    tran0.writeAction("slorii X16 X16 12 678")
    tran0.writeAction("slorii X16 X16 12 3109")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
