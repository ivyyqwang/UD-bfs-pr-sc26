from EFA_v2 import *
def evi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 2364
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 2342")
    tran0.writeAction("slorii X16 X16 12 1760")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("slorii X16 X16 12 2864")
    tran0.writeAction("slorii X16 X16 12 3318")
    tran0.writeAction("movir X17 -27369")
    tran0.writeAction("slorii X17 X17 12 3685")
    tran0.writeAction("slorii X17 X17 12 426")
    tran0.writeAction("slorii X17 X17 12 3463")
    tran0.writeAction("slorii X17 X17 12 2203")
    tran0.writeAction("evi X16 X17 2364 2")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
