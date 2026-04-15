from EFA_v2 import *
def sr_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 32473")
    tran0.writeAction("slorii X16 X16 12 2874")
    tran0.writeAction("slorii X16 X16 12 4080")
    tran0.writeAction("slorii X16 X16 12 3084")
    tran0.writeAction("slorii X16 X16 12 1408")
    tran0.writeAction("movir X17 -13040")
    tran0.writeAction("slorii X17 X17 12 2022")
    tran0.writeAction("slorii X17 X17 12 1147")
    tran0.writeAction("slorii X17 X17 12 1655")
    tran0.writeAction("slorii X17 X17 12 3273")
    tran0.writeAction("movir X18 6111")
    tran0.writeAction("slorii X18 X18 12 2451")
    tran0.writeAction("slorii X18 X18 12 1107")
    tran0.writeAction("slorii X18 X18 12 1915")
    tran0.writeAction("slorii X18 X18 12 1742")
    tran0.writeAction("sr X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
