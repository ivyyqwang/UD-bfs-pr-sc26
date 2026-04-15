from EFA_v2 import *
def sli_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -20782")
    tran0.writeAction("slorii X16 X16 12 2711")
    tran0.writeAction("slorii X16 X16 12 723")
    tran0.writeAction("slorii X16 X16 12 2555")
    tran0.writeAction("slorii X16 X16 12 1633")
    tran0.writeAction("movir X17 23133")
    tran0.writeAction("slorii X17 X17 12 2561")
    tran0.writeAction("slorii X17 X17 12 878")
    tran0.writeAction("slorii X17 X17 12 1720")
    tran0.writeAction("slorii X17 X17 12 3778")
    tran0.writeAction("sli X16 X17 29")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
