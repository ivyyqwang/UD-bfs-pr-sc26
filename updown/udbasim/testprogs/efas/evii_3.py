from EFA_v2 import *
def evii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 838091
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -1870")
    tran0.writeAction("slorii X16 X16 12 1802")
    tran0.writeAction("slorii X16 X16 12 2426")
    tran0.writeAction("slorii X16 X16 12 1413")
    tran0.writeAction("slorii X16 X16 12 492")
    tran0.writeAction("movir X17 -21824")
    tran0.writeAction("slorii X17 X17 12 1756")
    tran0.writeAction("slorii X17 X17 12 1914")
    tran0.writeAction("slorii X17 X17 12 734")
    tran0.writeAction("slorii X17 X17 12 3778")
    tran0.writeAction("evii X16 838091 228 5")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
