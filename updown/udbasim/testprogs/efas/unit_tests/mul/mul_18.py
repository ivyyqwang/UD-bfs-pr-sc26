from EFA_v2 import *
def mul_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5504123380535208260, 3591536540218201238]
    tran0.writeAction("movir X16 19554")
    tran0.writeAction("slorii X16 X16 12 2352")
    tran0.writeAction("slorii X16 X16 12 3440")
    tran0.writeAction("slorii X16 X16 12 2962")
    tran0.writeAction("slorii X16 X16 12 2372")
    tran0.writeAction("movir X17 12759")
    tran0.writeAction("slorii X17 X17 12 2871")
    tran0.writeAction("slorii X17 X17 12 1117")
    tran0.writeAction("slorii X17 X17 12 2217")
    tran0.writeAction("slorii X17 X17 12 1174")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
