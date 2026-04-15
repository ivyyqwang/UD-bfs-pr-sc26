from EFA_v2 import *
def fmadd_32_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [27516212, 4232678498, 2452120618]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 1")
    tran0.writeAction("slorii X16 X16 12 2621")
    tran0.writeAction("slorii X16 X16 12 3380")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 252")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 12 3170")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 146")
    tran0.writeAction("slorii X18 X18 12 646")
    tran0.writeAction("slorii X18 X18 12 1066")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
