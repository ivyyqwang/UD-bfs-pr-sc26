from EFA_v2 import *
def fmadd_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [937933704, 2568022011, 541497379]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 55")
    tran0.writeAction("slorii X16 X16 12 3707")
    tran0.writeAction("slorii X16 X16 12 2952")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 153")
    tran0.writeAction("slorii X17 X17 12 270")
    tran0.writeAction("slorii X17 X17 12 2043")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 32")
    tran0.writeAction("slorii X18 X18 12 1129")
    tran0.writeAction("slorii X18 X18 12 2083")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
