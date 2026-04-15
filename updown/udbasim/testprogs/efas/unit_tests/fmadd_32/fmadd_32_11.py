from EFA_v2 import *
def fmadd_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3320836807, 1875171160, 1161112607]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("slorii X16 X16 12 3839")
    tran0.writeAction("slorii X16 X16 12 711")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 111")
    tran0.writeAction("slorii X17 X17 12 3149")
    tran0.writeAction("slorii X17 X17 12 1880")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 69")
    tran0.writeAction("slorii X18 X18 12 850")
    tran0.writeAction("slorii X18 X18 12 3103")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
