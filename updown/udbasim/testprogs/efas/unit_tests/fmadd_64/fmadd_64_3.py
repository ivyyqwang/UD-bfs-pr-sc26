from EFA_v2 import *
def fmadd_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16551779762806447442, 8671288703276736685, 263915821941048162]
    tran0.writeAction("movir X16 58803")
    tran0.writeAction("slorii X16 X16 12 3007")
    tran0.writeAction("slorii X16 X16 12 4042")
    tran0.writeAction("slorii X16 X16 12 2365")
    tran0.writeAction("slorii X16 X16 12 3410")
    tran0.writeAction("movir X17 30806")
    tran0.writeAction("slorii X17 X17 12 2482")
    tran0.writeAction("slorii X17 X17 12 535")
    tran0.writeAction("slorii X17 X17 12 2734")
    tran0.writeAction("slorii X17 X17 12 173")
    tran0.writeAction("movir X18 937")
    tran0.writeAction("slorii X18 X18 12 2528")
    tran0.writeAction("slorii X18 X18 12 2737")
    tran0.writeAction("slorii X18 X18 12 1644")
    tran0.writeAction("slorii X18 X18 12 866")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
