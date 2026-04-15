from EFA_v2 import *
def mul_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7600513710402301819, -5795423816822933017]
    tran0.writeAction("movir X16 27002")
    tran0.writeAction("slorii X16 X16 12 1839")
    tran0.writeAction("slorii X16 X16 12 843")
    tran0.writeAction("slorii X16 X16 12 62")
    tran0.writeAction("slorii X16 X16 12 3963")
    tran0.writeAction("movir X17 44946")
    tran0.writeAction("slorii X17 X17 12 2123")
    tran0.writeAction("slorii X17 X17 12 3707")
    tran0.writeAction("slorii X17 X17 12 1763")
    tran0.writeAction("slorii X17 X17 12 2535")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
