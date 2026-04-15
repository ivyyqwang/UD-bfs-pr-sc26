from EFA_v2 import *
def fmul_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12859991709107698720, 10275253530275532137]
    tran0.writeAction("movir X16 45687")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 771")
    tran0.writeAction("slorii X16 X16 12 3411")
    tran0.writeAction("slorii X16 X16 12 3104")
    tran0.writeAction("movir X17 36505")
    tran0.writeAction("slorii X17 X17 12 138")
    tran0.writeAction("slorii X17 X17 12 1321")
    tran0.writeAction("slorii X17 X17 12 620")
    tran0.writeAction("slorii X17 X17 12 3433")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
