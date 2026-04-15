from EFA_v2 import *
def fmul_32_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [240456006, 1644825298]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 14")
    tran0.writeAction("slorii X16 X16 12 1361")
    tran0.writeAction("slorii X16 X16 12 326")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 98")
    tran0.writeAction("slorii X17 X17 12 160")
    tran0.writeAction("slorii X17 X17 12 2770")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
