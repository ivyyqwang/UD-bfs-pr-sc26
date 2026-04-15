from EFA_v2 import *
def slandi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -10318")
    tran0.writeAction("slorii X16 X16 12 3272")
    tran0.writeAction("slorii X16 X16 12 3202")
    tran0.writeAction("slorii X16 X16 12 2531")
    tran0.writeAction("slorii X16 X16 12 1561")
    tran0.writeAction("movir X17 14618")
    tran0.writeAction("slorii X17 X17 12 2257")
    tran0.writeAction("slorii X17 X17 12 1696")
    tran0.writeAction("slorii X17 X17 12 2876")
    tran0.writeAction("slorii X17 X17 12 915")
    tran0.writeAction("slandi X16 X17 22")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
