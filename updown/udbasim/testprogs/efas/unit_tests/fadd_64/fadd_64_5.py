from EFA_v2 import *
def fadd_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10405979810633571282, 5449795372315544291]
    tran0.writeAction("movir X16 36969")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("slorii X16 X16 12 296")
    tran0.writeAction("slorii X16 X16 12 2869")
    tran0.writeAction("slorii X16 X16 12 3026")
    tran0.writeAction("movir X17 19361")
    tran0.writeAction("slorii X17 X17 12 2304")
    tran0.writeAction("slorii X17 X17 12 1105")
    tran0.writeAction("slorii X17 X17 12 1784")
    tran0.writeAction("slorii X17 X17 12 2787")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
