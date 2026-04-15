from EFA_v2 import *
def fmadd_32_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2551674949, 2396986343, 3314296422]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("slorii X16 X16 12 375")
    tran0.writeAction("slorii X16 X16 12 2117")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 142")
    tran0.writeAction("slorii X17 X17 12 3569")
    tran0.writeAction("slorii X17 X17 12 3047")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 197")
    tran0.writeAction("slorii X18 X18 12 2242")
    tran0.writeAction("slorii X18 X18 12 1638")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
