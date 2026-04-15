from EFA_v2 import *
def and_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -10360")
    tran0.writeAction("slorii X16 X16 12 3405")
    tran0.writeAction("slorii X16 X16 12 1641")
    tran0.writeAction("slorii X16 X16 12 2604")
    tran0.writeAction("slorii X16 X16 12 2864")
    tran0.writeAction("movir X17 -20709")
    tran0.writeAction("slorii X17 X17 12 667")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("slorii X17 X17 12 1420")
    tran0.writeAction("slorii X17 X17 12 474")
    tran0.writeAction("movir X18 -17297")
    tran0.writeAction("slorii X18 X18 12 4010")
    tran0.writeAction("slorii X18 X18 12 3984")
    tran0.writeAction("slorii X18 X18 12 2635")
    tran0.writeAction("slorii X18 X18 12 1053")
    tran0.writeAction("and X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
