from EFA_v2 import *
def evlb_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 739034
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -346")
    tran0.writeAction("slorii X16 X16 12 1810")
    tran0.writeAction("slorii X16 X16 12 2378")
    tran0.writeAction("slorii X16 X16 12 3243")
    tran0.writeAction("slorii X16 X16 12 3262")
    tran0.writeAction("movir X17 -22625")
    tran0.writeAction("slorii X17 X17 12 1160")
    tran0.writeAction("slorii X17 X17 12 2332")
    tran0.writeAction("slorii X17 X17 12 2442")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("evlb X16 739034")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
