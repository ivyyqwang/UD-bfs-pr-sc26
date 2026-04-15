from EFA_v2 import *
def fmadd_64_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1935481897067183109, 1726718464695984529, 8770468313008318421]
    tran0.writeAction("movir X16 6876")
    tran0.writeAction("slorii X16 X16 12 872")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 3639")
    tran0.writeAction("slorii X16 X16 12 3077")
    tran0.writeAction("movir X17 6134")
    tran0.writeAction("slorii X17 X17 12 2196")
    tran0.writeAction("slorii X17 X17 12 2955")
    tran0.writeAction("slorii X17 X17 12 1278")
    tran0.writeAction("slorii X17 X17 12 401")
    tran0.writeAction("movir X18 31158")
    tran0.writeAction("slorii X18 X18 12 3943")
    tran0.writeAction("slorii X18 X18 12 1654")
    tran0.writeAction("slorii X18 X18 12 2786")
    tran0.writeAction("slorii X18 X18 12 2005")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
