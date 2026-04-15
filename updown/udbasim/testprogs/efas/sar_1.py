from EFA_v2 import *
def sar_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 18736")
    tran0.writeAction("slorii X16 X16 12 68")
    tran0.writeAction("slorii X16 X16 12 215")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("slorii X16 X16 12 2562")
    tran0.writeAction("movir X17 2636")
    tran0.writeAction("slorii X17 X17 12 3516")
    tran0.writeAction("slorii X17 X17 12 1779")
    tran0.writeAction("slorii X17 X17 12 2111")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("movir X18 24770")
    tran0.writeAction("slorii X18 X18 12 3374")
    tran0.writeAction("slorii X18 X18 12 746")
    tran0.writeAction("slorii X18 X18 12 1468")
    tran0.writeAction("slorii X18 X18 12 2036")
    tran0.writeAction("sar X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
