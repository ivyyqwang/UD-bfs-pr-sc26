from EFA_v2 import *
def sl_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -21668")
    tran0.writeAction("slorii X16 X16 12 1080")
    tran0.writeAction("slorii X16 X16 12 3350")
    tran0.writeAction("slorii X16 X16 12 3860")
    tran0.writeAction("slorii X16 X16 12 232")
    tran0.writeAction("movir X17 -15038")
    tran0.writeAction("slorii X17 X17 12 704")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 12 2268")
    tran0.writeAction("slorii X17 X17 12 3017")
    tran0.writeAction("movir X18 -26495")
    tran0.writeAction("slorii X18 X18 12 3825")
    tran0.writeAction("slorii X18 X18 12 88")
    tran0.writeAction("slorii X18 X18 12 1662")
    tran0.writeAction("slorii X18 X18 12 1047")
    tran0.writeAction("sl X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
