from EFA_v2 import *
def srorii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 29440")
    tran0.writeAction("slorii X16 X16 12 3210")
    tran0.writeAction("slorii X16 X16 12 1920")
    tran0.writeAction("slorii X16 X16 12 1982")
    tran0.writeAction("slorii X16 X16 12 3729")
    tran0.writeAction("movir X17 28113")
    tran0.writeAction("slorii X17 X17 12 2094")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("slorii X17 X17 12 1867")
    tran0.writeAction("slorii X17 X17 12 1367")
    tran0.writeAction("srorii X16 X17 5 2252")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
