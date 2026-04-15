from EFA_v2 import *
def evi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 2202
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -23495")
    tran0.writeAction("slorii X16 X16 12 318")
    tran0.writeAction("slorii X16 X16 12 2295")
    tran0.writeAction("slorii X16 X16 12 1336")
    tran0.writeAction("slorii X16 X16 12 2016")
    tran0.writeAction("movir X17 20327")
    tran0.writeAction("slorii X17 X17 12 855")
    tran0.writeAction("slorii X17 X17 12 1062")
    tran0.writeAction("slorii X17 X17 12 3791")
    tran0.writeAction("slorii X17 X17 12 2641")
    tran0.writeAction("evi X16 X17 2202 8")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
