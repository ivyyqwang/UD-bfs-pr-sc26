from EFA_v2 import *
def fmadd_32_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1182755024, 4164745959, 2475940868]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 70")
    tran0.writeAction("slorii X16 X16 12 2038")
    tran0.writeAction("slorii X16 X16 12 2256")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 248")
    tran0.writeAction("slorii X17 X17 12 975")
    tran0.writeAction("slorii X17 X17 12 2791")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 147")
    tran0.writeAction("slorii X18 X18 12 2365")
    tran0.writeAction("slorii X18 X18 12 3076")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
