from EFA_v2 import *
def slandii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 5196")
    tran0.writeAction("slorii X16 X16 12 848")
    tran0.writeAction("slorii X16 X16 12 3120")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("slorii X16 X16 12 3933")
    tran0.writeAction("movir X17 -13468")
    tran0.writeAction("slorii X17 X17 12 2619")
    tran0.writeAction("slorii X17 X17 12 822")
    tran0.writeAction("slorii X17 X17 12 1430")
    tran0.writeAction("slorii X17 X17 12 4078")
    tran0.writeAction("slandii X16 X17 13 2865")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
