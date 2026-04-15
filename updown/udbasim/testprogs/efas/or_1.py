from EFA_v2 import *
def or_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -10370")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 4082")
    tran0.writeAction("slorii X16 X16 12 1024")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("movir X17 -1560")
    tran0.writeAction("slorii X17 X17 12 1554")
    tran0.writeAction("slorii X17 X17 12 1855")
    tran0.writeAction("slorii X17 X17 12 2968")
    tran0.writeAction("slorii X17 X17 12 773")
    tran0.writeAction("movir X18 28892")
    tran0.writeAction("slorii X18 X18 12 934")
    tran0.writeAction("slorii X18 X18 12 2088")
    tran0.writeAction("slorii X18 X18 12 1967")
    tran0.writeAction("slorii X18 X18 12 1507")
    tran0.writeAction("or X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
