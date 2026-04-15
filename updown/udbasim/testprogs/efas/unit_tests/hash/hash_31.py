from EFA_v2 import *
def hash_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2505143550728206734, 7832129392224626347]
    tran0.writeAction("movir X16 56635")
    tran0.writeAction("slorii X16 X16 12 3859")
    tran0.writeAction("slorii X16 X16 12 1699")
    tran0.writeAction("slorii X16 X16 12 1984")
    tran0.writeAction("slorii X16 X16 12 1650")
    tran0.writeAction("movir X17 27825")
    tran0.writeAction("slorii X17 X17 12 1282")
    tran0.writeAction("slorii X17 X17 12 3986")
    tran0.writeAction("slorii X17 X17 12 1822")
    tran0.writeAction("slorii X17 X17 12 1707")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
