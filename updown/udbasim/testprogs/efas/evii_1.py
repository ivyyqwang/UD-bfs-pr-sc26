from EFA_v2 import *
def evii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 462712
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -16993")
    tran0.writeAction("slorii X16 X16 12 2718")
    tran0.writeAction("slorii X16 X16 12 423")
    tran0.writeAction("slorii X16 X16 12 4048")
    tran0.writeAction("slorii X16 X16 12 1090")
    tran0.writeAction("movir X17 -31045")
    tran0.writeAction("slorii X17 X17 12 266")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 12 2649")
    tran0.writeAction("slorii X17 X17 12 545")
    tran0.writeAction("evii X16 462712 3337 5")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
