from EFA_v2 import *
def fadd_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13089543187011558702, 16557730239162631881]
    tran0.writeAction("movir X16 46503")
    tran0.writeAction("slorii X16 X16 12 1634")
    tran0.writeAction("slorii X16 X16 12 3421")
    tran0.writeAction("slorii X16 X16 12 3925")
    tran0.writeAction("slorii X16 X16 12 3374")
    tran0.writeAction("movir X17 58824")
    tran0.writeAction("slorii X17 X17 12 3582")
    tran0.writeAction("slorii X17 X17 12 3336")
    tran0.writeAction("slorii X17 X17 12 132")
    tran0.writeAction("slorii X17 X17 12 1737")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
