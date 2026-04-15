from EFA_v2 import *
def fmadd_32_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1229148499, 300362786, 169541215]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 73")
    tran0.writeAction("slorii X16 X16 12 1077")
    tran0.writeAction("slorii X16 X16 12 339")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 17")
    tran0.writeAction("slorii X17 X17 12 3698")
    tran0.writeAction("slorii X17 X17 12 3106")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 10")
    tran0.writeAction("slorii X18 X18 12 431")
    tran0.writeAction("slorii X18 X18 12 3679")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
