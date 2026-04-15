from EFA_v2 import *
def slandii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -29100")
    tran0.writeAction("slorii X16 X16 12 981")
    tran0.writeAction("slorii X16 X16 12 3395")
    tran0.writeAction("slorii X16 X16 12 2988")
    tran0.writeAction("slorii X16 X16 12 2901")
    tran0.writeAction("movir X17 -7598")
    tran0.writeAction("slorii X17 X17 12 680")
    tran0.writeAction("slorii X17 X17 12 2148")
    tran0.writeAction("slorii X17 X17 12 3572")
    tran0.writeAction("slorii X17 X17 12 2181")
    tran0.writeAction("slandii X16 X17 7 3433")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
