from EFA_v2 import *
def fmadd_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [220662352654699771, 11353306054820887457, 9176838319221932943]
    tran0.writeAction("movir X16 783")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("slorii X16 X16 12 3481")
    tran0.writeAction("slorii X16 X16 12 1168")
    tran0.writeAction("slorii X16 X16 12 3323")
    tran0.writeAction("movir X17 40335")
    tran0.writeAction("slorii X17 X17 12 187")
    tran0.writeAction("slorii X17 X17 12 1111")
    tran0.writeAction("slorii X17 X17 12 3647")
    tran0.writeAction("slorii X17 X17 12 2977")
    tran0.writeAction("movir X18 32602")
    tran0.writeAction("slorii X18 X18 12 2781")
    tran0.writeAction("slorii X18 X18 12 1170")
    tran0.writeAction("slorii X18 X18 12 1704")
    tran0.writeAction("slorii X18 X18 12 911")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
