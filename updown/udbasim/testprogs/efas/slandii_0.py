from EFA_v2 import *
def slandii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -16870")
    tran0.writeAction("slorii X16 X16 12 1319")
    tran0.writeAction("slorii X16 X16 12 1463")
    tran0.writeAction("slorii X16 X16 12 3740")
    tran0.writeAction("slorii X16 X16 12 1882")
    tran0.writeAction("movir X17 -21556")
    tran0.writeAction("slorii X17 X17 12 2180")
    tran0.writeAction("slorii X17 X17 12 1540")
    tran0.writeAction("slorii X17 X17 12 2436")
    tran0.writeAction("slorii X17 X17 12 1021")
    tran0.writeAction("slandii X16 X17 11 1769")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
