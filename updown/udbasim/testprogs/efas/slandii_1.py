from EFA_v2 import *
def slandii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 9305")
    tran0.writeAction("slorii X16 X16 12 3554")
    tran0.writeAction("slorii X16 X16 12 806")
    tran0.writeAction("slorii X16 X16 12 1064")
    tran0.writeAction("slorii X16 X16 12 3075")
    tran0.writeAction("movir X17 -3494")
    tran0.writeAction("slorii X17 X17 12 1860")
    tran0.writeAction("slorii X17 X17 12 3162")
    tran0.writeAction("slorii X17 X17 12 2592")
    tran0.writeAction("slorii X17 X17 12 3858")
    tran0.writeAction("slandii X16 X17 12 2467")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
