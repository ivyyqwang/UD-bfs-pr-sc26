from EFA_v2 import *
def sl_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 7387")
    tran0.writeAction("slorii X16 X16 12 189")
    tran0.writeAction("slorii X16 X16 12 748")
    tran0.writeAction("slorii X16 X16 12 546")
    tran0.writeAction("slorii X16 X16 12 1616")
    tran0.writeAction("movir X17 29555")
    tran0.writeAction("slorii X17 X17 12 3074")
    tran0.writeAction("slorii X17 X17 12 267")
    tran0.writeAction("slorii X17 X17 12 771")
    tran0.writeAction("slorii X17 X17 12 4029")
    tran0.writeAction("movir X18 -21163")
    tran0.writeAction("slorii X18 X18 12 3368")
    tran0.writeAction("slorii X18 X18 12 3891")
    tran0.writeAction("slorii X18 X18 12 4004")
    tran0.writeAction("slorii X18 X18 12 106")
    tran0.writeAction("sl X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
