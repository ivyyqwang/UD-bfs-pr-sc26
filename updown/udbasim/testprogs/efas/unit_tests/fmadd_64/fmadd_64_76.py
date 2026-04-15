from EFA_v2 import *
def fmadd_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7860271490256315825, 14884961611523399018, 10748976558524807745]
    tran0.writeAction("movir X16 27925")
    tran0.writeAction("slorii X16 X16 12 1204")
    tran0.writeAction("slorii X16 X16 12 1630")
    tran0.writeAction("slorii X16 X16 12 3514")
    tran0.writeAction("slorii X16 X16 12 1457")
    tran0.writeAction("movir X17 52882")
    tran0.writeAction("slorii X17 X17 12 27")
    tran0.writeAction("slorii X17 X17 12 2246")
    tran0.writeAction("slorii X17 X17 12 729")
    tran0.writeAction("slorii X17 X17 12 3434")
    tran0.writeAction("movir X18 38188")
    tran0.writeAction("slorii X18 X18 12 147")
    tran0.writeAction("slorii X18 X18 12 2749")
    tran0.writeAction("slorii X18 X18 12 3571")
    tran0.writeAction("slorii X18 X18 12 2625")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
