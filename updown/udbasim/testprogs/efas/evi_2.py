from EFA_v2 import *
def evi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 1824
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -719")
    tran0.writeAction("slorii X16 X16 12 647")
    tran0.writeAction("slorii X16 X16 12 2268")
    tran0.writeAction("slorii X16 X16 12 3986")
    tran0.writeAction("slorii X16 X16 12 1253")
    tran0.writeAction("movir X17 -2385")
    tran0.writeAction("slorii X17 X17 12 1104")
    tran0.writeAction("slorii X17 X17 12 461")
    tran0.writeAction("slorii X17 X17 12 1719")
    tran0.writeAction("slorii X17 X17 12 2435")
    tran0.writeAction("evi X16 X17 1824 1")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
