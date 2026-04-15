from EFA_v2 import *
def fmadd_32_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2805908124, 842626795, 3517782238]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("slorii X16 X16 12 1004")
    tran0.writeAction("slorii X16 X16 12 668")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 50")
    tran0.writeAction("slorii X17 X17 12 919")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 209")
    tran0.writeAction("slorii X18 X18 12 2769")
    tran0.writeAction("slorii X18 X18 12 2270")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
