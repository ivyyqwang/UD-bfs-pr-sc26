from EFA_v2 import *
def slori_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 9935")
    tran0.writeAction("slorii X16 X16 12 2666")
    tran0.writeAction("slorii X16 X16 12 3598")
    tran0.writeAction("slorii X16 X16 12 1776")
    tran0.writeAction("slorii X16 X16 12 3645")
    tran0.writeAction("movir X17 20595")
    tran0.writeAction("slorii X17 X17 12 1198")
    tran0.writeAction("slorii X17 X17 12 3187")
    tran0.writeAction("slorii X17 X17 12 1625")
    tran0.writeAction("slorii X17 X17 12 264")
    tran0.writeAction("slori X16 X17 33")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
