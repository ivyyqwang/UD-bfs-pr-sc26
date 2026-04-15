from EFA_v2 import *
def fmadd_32_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3459164643, 821277633, 915213522]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 206")
    tran0.writeAction("slorii X16 X16 12 746")
    tran0.writeAction("slorii X16 X16 12 2531")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 48")
    tran0.writeAction("slorii X17 X17 12 3899")
    tran0.writeAction("slorii X17 X17 12 961")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 54")
    tran0.writeAction("slorii X18 X18 12 2256")
    tran0.writeAction("slorii X18 X18 12 3282")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
