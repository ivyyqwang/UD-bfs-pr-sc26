from EFA_v2 import *
def evii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 3000
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -3512")
    tran0.writeAction("slorii X16 X16 12 1478")
    tran0.writeAction("slorii X16 X16 12 2679")
    tran0.writeAction("slorii X16 X16 12 2598")
    tran0.writeAction("slorii X16 X16 12 3158")
    tran0.writeAction("movir X17 27591")
    tran0.writeAction("slorii X17 X17 12 2554")
    tran0.writeAction("slorii X17 X17 12 606")
    tran0.writeAction("slorii X17 X17 12 1776")
    tran0.writeAction("slorii X17 X17 12 3306")
    tran0.writeAction("evii X16 3000 2556 10")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
