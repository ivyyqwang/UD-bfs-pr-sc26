from EFA_v2 import *
def fmadd_32_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3981961102, 2633734184, 2611457715]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 237")
    tran0.writeAction("slorii X16 X16 12 1406")
    tran0.writeAction("slorii X16 X16 12 1934")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 156")
    tran0.writeAction("slorii X17 X17 12 4025")
    tran0.writeAction("slorii X17 X17 12 2088")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 155")
    tran0.writeAction("slorii X18 X18 12 2682")
    tran0.writeAction("slorii X18 X18 12 3763")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
