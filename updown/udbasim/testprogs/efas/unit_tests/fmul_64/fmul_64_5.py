from EFA_v2 import *
def fmul_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6276590293365829889, 1414369492898450272]
    tran0.writeAction("movir X16 22298")
    tran0.writeAction("slorii X16 X16 12 3801")
    tran0.writeAction("slorii X16 X16 12 3572")
    tran0.writeAction("slorii X16 X16 12 3011")
    tran0.writeAction("slorii X16 X16 12 257")
    tran0.writeAction("movir X17 5024")
    tran0.writeAction("slorii X17 X17 12 3480")
    tran0.writeAction("slorii X17 X17 12 3941")
    tran0.writeAction("slorii X17 X17 12 1480")
    tran0.writeAction("slorii X17 X17 12 2912")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
