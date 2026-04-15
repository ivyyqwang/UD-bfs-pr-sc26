from EFA_v2 import *
def srandii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 3635")
    tran0.writeAction("slorii X16 X16 12 2516")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("slorii X16 X16 12 1320")
    tran0.writeAction("slorii X16 X16 12 1266")
    tran0.writeAction("movir X17 23821")
    tran0.writeAction("slorii X17 X17 12 358")
    tran0.writeAction("slorii X17 X17 12 437")
    tran0.writeAction("slorii X17 X17 12 1115")
    tran0.writeAction("slorii X17 X17 12 2546")
    tran0.writeAction("srandii X16 X17 14 2521")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
