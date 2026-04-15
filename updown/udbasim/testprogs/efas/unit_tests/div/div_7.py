from EFA_v2 import *
def div_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1799889706502514631, 8209495237626632353]
    tran0.writeAction("movir X16 59141")
    tran0.writeAction("slorii X16 X16 12 2077")
    tran0.writeAction("slorii X16 X16 12 2337")
    tran0.writeAction("slorii X16 X16 12 145")
    tran0.writeAction("slorii X16 X16 12 2105")
    tran0.writeAction("movir X17 29165")
    tran0.writeAction("slorii X17 X17 12 4038")
    tran0.writeAction("slorii X17 X17 12 3135")
    tran0.writeAction("slorii X17 X17 12 4081")
    tran0.writeAction("slorii X17 X17 12 2209")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
