from EFA_v2 import *
def fmadd_32_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2774166543, 2715808694, 1719867155]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("slorii X16 X16 12 1446")
    tran0.writeAction("slorii X16 X16 12 3087")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 161")
    tran0.writeAction("slorii X17 X17 12 3583")
    tran0.writeAction("slorii X17 X17 12 950")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 102")
    tran0.writeAction("slorii X18 X18 12 2097")
    tran0.writeAction("slorii X18 X18 12 1811")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
