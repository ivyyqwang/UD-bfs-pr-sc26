from EFA_v2 import *
def fmadd_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10913186048578676339, 13492470360414543251, 4531075928372709658]
    tran0.writeAction("movir X16 38771")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("slorii X16 X16 12 1025")
    tran0.writeAction("slorii X16 X16 12 1150")
    tran0.writeAction("slorii X16 X16 12 1651")
    tran0.writeAction("movir X17 47934")
    tran0.writeAction("slorii X17 X17 12 3620")
    tran0.writeAction("slorii X17 X17 12 3710")
    tran0.writeAction("slorii X17 X17 12 4077")
    tran0.writeAction("slorii X17 X17 12 3475")
    tran0.writeAction("movir X18 16097")
    tran0.writeAction("slorii X18 X18 12 2520")
    tran0.writeAction("slorii X18 X18 12 3288")
    tran0.writeAction("slorii X18 X18 12 4008")
    tran0.writeAction("slorii X18 X18 12 2330")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
