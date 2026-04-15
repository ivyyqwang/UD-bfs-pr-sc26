from EFA_v2 import *
def sub_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8593574443801129391, 9119905103850466625]
    tran0.writeAction("movir X16 30530")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("slorii X16 X16 12 3337")
    tran0.writeAction("slorii X16 X16 12 2627")
    tran0.writeAction("slorii X16 X16 12 431")
    tran0.writeAction("movir X17 32400")
    tran0.writeAction("slorii X17 X17 12 1685")
    tran0.writeAction("slorii X17 X17 12 3940")
    tran0.writeAction("slorii X17 X17 12 1142")
    tran0.writeAction("slorii X17 X17 12 3393")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
