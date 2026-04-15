from EFA_v2 import *
def fdiv_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4596339965192037239, 12419162931178110195]
    tran0.writeAction("movir X16 16329")
    tran0.writeAction("slorii X16 X16 12 1965")
    tran0.writeAction("slorii X16 X16 12 2188")
    tran0.writeAction("slorii X16 X16 12 830")
    tran0.writeAction("slorii X16 X16 12 887")
    tran0.writeAction("movir X17 44121")
    tran0.writeAction("slorii X17 X17 12 2990")
    tran0.writeAction("slorii X17 X17 12 744")
    tran0.writeAction("slorii X17 X17 12 2335")
    tran0.writeAction("slorii X17 X17 12 3315")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
