from EFA_v2 import *
def mul_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5240726345422233295, 3011068935576779567]
    tran0.writeAction("movir X16 46917")
    tran0.writeAction("slorii X16 X16 12 818")
    tran0.writeAction("slorii X16 X16 12 1992")
    tran0.writeAction("slorii X16 X16 12 314")
    tran0.writeAction("slorii X16 X16 12 305")
    tran0.writeAction("movir X17 10697")
    tran0.writeAction("slorii X17 X17 12 1907")
    tran0.writeAction("slorii X17 X17 12 3675")
    tran0.writeAction("slorii X17 X17 12 1095")
    tran0.writeAction("slorii X17 X17 12 2863")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
