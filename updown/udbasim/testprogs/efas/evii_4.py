from EFA_v2 import *
def evii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 496296
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -25207")
    tran0.writeAction("slorii X16 X16 12 2191")
    tran0.writeAction("slorii X16 X16 12 3478")
    tran0.writeAction("slorii X16 X16 12 2512")
    tran0.writeAction("slorii X16 X16 12 2845")
    tran0.writeAction("movir X17 -960")
    tran0.writeAction("slorii X17 X17 12 2387")
    tran0.writeAction("slorii X17 X17 12 169")
    tran0.writeAction("slorii X17 X17 12 1326")
    tran0.writeAction("slorii X17 X17 12 1698")
    tran0.writeAction("evii X16 496296 3739 5")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
