from EFA_v2 import *
def div_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1437100302798933436, 2927144664345992119]
    tran0.writeAction("movir X16 60430")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("slorii X16 X16 12 897")
    tran0.writeAction("slorii X16 X16 12 259")
    tran0.writeAction("slorii X16 X16 12 580")
    tran0.writeAction("movir X17 10399")
    tran0.writeAction("slorii X17 X17 12 1257")
    tran0.writeAction("slorii X17 X17 12 68")
    tran0.writeAction("slorii X17 X17 12 2141")
    tran0.writeAction("slorii X17 X17 12 2999")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
