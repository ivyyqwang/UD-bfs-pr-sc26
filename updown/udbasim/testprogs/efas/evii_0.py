from EFA_v2 import *
def evii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 3441
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -10329")
    tran0.writeAction("slorii X16 X16 12 859")
    tran0.writeAction("slorii X16 X16 12 837")
    tran0.writeAction("slorii X16 X16 12 517")
    tran0.writeAction("slorii X16 X16 12 84")
    tran0.writeAction("movir X17 26277")
    tran0.writeAction("slorii X17 X17 12 354")
    tran0.writeAction("slorii X17 X17 12 2690")
    tran0.writeAction("slorii X17 X17 12 3372")
    tran0.writeAction("slorii X17 X17 12 1499")
    tran0.writeAction("evii X16 3441 275 6")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
