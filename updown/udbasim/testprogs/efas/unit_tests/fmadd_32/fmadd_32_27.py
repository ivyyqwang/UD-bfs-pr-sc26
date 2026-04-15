from EFA_v2 import *
def fmadd_32_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1627147355, 2382986389, 709337886]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 96")
    tran0.writeAction("slorii X16 X16 12 4036")
    tran0.writeAction("slorii X16 X16 12 3163")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 142")
    tran0.writeAction("slorii X17 X17 12 151")
    tran0.writeAction("slorii X17 X17 12 3221")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 42")
    tran0.writeAction("slorii X18 X18 12 1146")
    tran0.writeAction("slorii X18 X18 12 798")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
