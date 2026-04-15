from EFA_v2 import *
def sub_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2448755543054755619, 31929822399134458]
    tran0.writeAction("movir X16 56836")
    tran0.writeAction("slorii X16 X16 12 1116")
    tran0.writeAction("slorii X16 X16 12 3778")
    tran0.writeAction("slorii X16 X16 12 1853")
    tran0.writeAction("slorii X16 X16 12 2269")
    tran0.writeAction("movir X17 113")
    tran0.writeAction("slorii X17 X17 12 1792")
    tran0.writeAction("slorii X17 X17 12 281")
    tran0.writeAction("slorii X17 X17 12 3447")
    tran0.writeAction("slorii X17 X17 12 2810")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
