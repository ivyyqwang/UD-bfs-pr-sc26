from EFA_v2 import *
def slandi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 9616")
    tran0.writeAction("slorii X16 X16 12 3957")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("slorii X16 X16 12 3918")
    tran0.writeAction("slorii X16 X16 12 2324")
    tran0.writeAction("movir X17 28473")
    tran0.writeAction("slorii X17 X17 12 3083")
    tran0.writeAction("slorii X17 X17 12 3672")
    tran0.writeAction("slorii X17 X17 12 1235")
    tran0.writeAction("slorii X17 X17 12 3123")
    tran0.writeAction("slandi X16 X17 3")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
