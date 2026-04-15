from EFA_v2 import *
def fmadd_32_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [609551342, 1933769806, 179916611]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 36")
    tran0.writeAction("slorii X16 X16 12 1360")
    tran0.writeAction("slorii X16 X16 12 1006")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 115")
    tran0.writeAction("slorii X17 X17 12 1071")
    tran0.writeAction("slorii X17 X17 12 3150")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 10")
    tran0.writeAction("slorii X18 X18 12 2964")
    tran0.writeAction("slorii X18 X18 12 3907")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
