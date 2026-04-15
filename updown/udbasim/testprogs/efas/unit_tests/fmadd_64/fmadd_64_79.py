from EFA_v2 import *
def fmadd_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2914374369976612683, 10937868981630312187, 1501027993331508574]
    tran0.writeAction("movir X16 10353")
    tran0.writeAction("slorii X16 X16 12 3840")
    tran0.writeAction("slorii X16 X16 12 3176")
    tran0.writeAction("slorii X16 X16 12 3927")
    tran0.writeAction("slorii X16 X16 12 1867")
    tran0.writeAction("movir X17 38859")
    tran0.writeAction("slorii X17 X17 12 478")
    tran0.writeAction("slorii X17 X17 12 817")
    tran0.writeAction("slorii X17 X17 12 3433")
    tran0.writeAction("slorii X17 X17 12 3835")
    tran0.writeAction("movir X18 5332")
    tran0.writeAction("slorii X18 X18 12 2960")
    tran0.writeAction("slorii X18 X18 12 468")
    tran0.writeAction("slorii X18 X18 12 1810")
    tran0.writeAction("slorii X18 X18 12 1374")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
