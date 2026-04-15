from EFA_v2 import *
def fmul_64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11964195457773142972, 3313305033671496116]
    tran0.writeAction("movir X16 42505")
    tran0.writeAction("slorii X16 X16 12 1478")
    tran0.writeAction("slorii X16 X16 12 315")
    tran0.writeAction("slorii X16 X16 12 3728")
    tran0.writeAction("slorii X16 X16 12 956")
    tran0.writeAction("movir X17 11771")
    tran0.writeAction("slorii X17 X17 12 917")
    tran0.writeAction("slorii X17 X17 12 3996")
    tran0.writeAction("slorii X17 X17 12 2061")
    tran0.writeAction("slorii X17 X17 12 436")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
