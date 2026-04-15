from EFA_v2 import *
def evlb_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 916387
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 24679")
    tran0.writeAction("slorii X16 X16 12 1206")
    tran0.writeAction("slorii X16 X16 12 517")
    tran0.writeAction("slorii X16 X16 12 2419")
    tran0.writeAction("slorii X16 X16 12 456")
    tran0.writeAction("movir X17 7465")
    tran0.writeAction("slorii X17 X17 12 3111")
    tran0.writeAction("slorii X17 X17 12 1888")
    tran0.writeAction("slorii X17 X17 12 2068")
    tran0.writeAction("slorii X17 X17 12 925")
    tran0.writeAction("evlb X16 916387")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
