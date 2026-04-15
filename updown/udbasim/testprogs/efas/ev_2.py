from EFA_v2 import *
def ev_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 766753
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 10034")
    tran0.writeAction("slorii X16 X16 12 3018")
    tran0.writeAction("slorii X16 X16 12 599")
    tran0.writeAction("slorii X16 X16 12 1586")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("movir X17 15661")
    tran0.writeAction("slorii X17 X17 12 3789")
    tran0.writeAction("slorii X17 X17 12 2589")
    tran0.writeAction("slorii X17 X17 12 3383")
    tran0.writeAction("slorii X17 X17 12 1502")
    tran0.writeAction("movir X18 -19738")
    tran0.writeAction("slorii X18 X18 12 3262")
    tran0.writeAction("slorii X18 X18 12 1278")
    tran0.writeAction("slorii X18 X18 12 955")
    tran0.writeAction("slorii X18 X18 12 801")
    tran0.writeAction("movir X19 -13686")
    tran0.writeAction("slorii X19 X19 12 3309")
    tran0.writeAction("slorii X19 X19 12 2216")
    tran0.writeAction("slorii X19 X19 12 767")
    tran0.writeAction("slorii X19 X19 12 3229")
    tran0.writeAction("ev X16 X17 X18 X19 4")
    tran0.writeAction(f"print '%d,%d,%d,%d' X16 X17 X18 X19")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
