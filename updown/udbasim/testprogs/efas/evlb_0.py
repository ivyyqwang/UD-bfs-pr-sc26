from EFA_v2 import *
def evlb_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 901863
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 6949")
    tran0.writeAction("slorii X16 X16 12 1210")
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("slorii X16 X16 12 192")
    tran0.writeAction("slorii X16 X16 12 384")
    tran0.writeAction("movir X17 19993")
    tran0.writeAction("slorii X17 X17 12 2838")
    tran0.writeAction("slorii X17 X17 12 3648")
    tran0.writeAction("slorii X17 X17 12 2835")
    tran0.writeAction("slorii X17 X17 12 1642")
    tran0.writeAction("evlb X16 901863")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
