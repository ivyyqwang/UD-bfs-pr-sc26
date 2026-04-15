from EFA_v2 import *
def fadd_64_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3953351628617380142, 10019724951143491859]
    tran0.writeAction("movir X16 14045")
    tran0.writeAction("slorii X16 X16 12 517")
    tran0.writeAction("slorii X16 X16 12 3143")
    tran0.writeAction("slorii X16 X16 12 3895")
    tran0.writeAction("slorii X16 X16 12 302")
    tran0.writeAction("movir X17 35597")
    tran0.writeAction("slorii X17 X17 12 876")
    tran0.writeAction("slorii X17 X17 12 412")
    tran0.writeAction("slorii X17 X17 12 106")
    tran0.writeAction("slorii X17 X17 12 2323")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
