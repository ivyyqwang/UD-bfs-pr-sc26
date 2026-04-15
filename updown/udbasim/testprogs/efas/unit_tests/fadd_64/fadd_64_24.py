from EFA_v2 import *
def fadd_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2283294185827866014, 2902556079380910641]
    tran0.writeAction("movir X16 8111")
    tran0.writeAction("slorii X16 X16 12 3647")
    tran0.writeAction("slorii X16 X16 12 1775")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("slorii X16 X16 12 1438")
    tran0.writeAction("movir X17 10311")
    tran0.writeAction("slorii X17 X17 12 3894")
    tran0.writeAction("slorii X17 X17 12 52")
    tran0.writeAction("slorii X17 X17 12 613")
    tran0.writeAction("slorii X17 X17 12 561")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
