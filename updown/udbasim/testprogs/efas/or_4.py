from EFA_v2 import *
def or_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -26035")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 608")
    tran0.writeAction("slorii X16 X16 12 2412")
    tran0.writeAction("slorii X16 X16 12 1332")
    tran0.writeAction("movir X17 -28964")
    tran0.writeAction("slorii X17 X17 12 3172")
    tran0.writeAction("slorii X17 X17 12 2345")
    tran0.writeAction("slorii X17 X17 12 3264")
    tran0.writeAction("slorii X17 X17 12 2550")
    tran0.writeAction("movir X18 10510")
    tran0.writeAction("slorii X18 X18 12 1228")
    tran0.writeAction("slorii X18 X18 12 1772")
    tran0.writeAction("slorii X18 X18 12 1573")
    tran0.writeAction("slorii X18 X18 12 2333")
    tran0.writeAction("or X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
