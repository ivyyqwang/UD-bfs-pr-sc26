from EFA_v2 import *
def fmadd_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3231380931, 242951767, 1354234881]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 192")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 14")
    tran0.writeAction("slorii X17 X17 12 1970")
    tran0.writeAction("slorii X17 X17 12 1623")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 80")
    tran0.writeAction("slorii X18 X18 12 2943")
    tran0.writeAction("slorii X18 X18 12 3073")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
