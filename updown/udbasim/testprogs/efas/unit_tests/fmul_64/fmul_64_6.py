from EFA_v2 import *
def fmul_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11807333879740778294, 7161080794785397265]
    tran0.writeAction("movir X16 41948")
    tran0.writeAction("slorii X16 X16 12 313")
    tran0.writeAction("slorii X16 X16 12 2830")
    tran0.writeAction("slorii X16 X16 12 1572")
    tran0.writeAction("slorii X16 X16 12 1846")
    tran0.writeAction("movir X17 25441")
    tran0.writeAction("slorii X17 X17 12 1104")
    tran0.writeAction("slorii X17 X17 12 2741")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 12 2577")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
