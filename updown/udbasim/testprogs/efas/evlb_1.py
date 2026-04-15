from EFA_v2 import *
def evlb_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 259136
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -1481")
    tran0.writeAction("slorii X16 X16 12 3886")
    tran0.writeAction("slorii X16 X16 12 1423")
    tran0.writeAction("slorii X16 X16 12 3261")
    tran0.writeAction("slorii X16 X16 12 737")
    tran0.writeAction("movir X17 -20830")
    tran0.writeAction("slorii X17 X17 12 1752")
    tran0.writeAction("slorii X17 X17 12 3007")
    tran0.writeAction("slorii X17 X17 12 2313")
    tran0.writeAction("slorii X17 X17 12 3323")
    tran0.writeAction("evlb X16 259136")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
