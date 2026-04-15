from EFA_v2 import *
def sr_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 11166")
    tran0.writeAction("slorii X16 X16 12 2500")
    tran0.writeAction("slorii X16 X16 12 684")
    tran0.writeAction("slorii X16 X16 12 2948")
    tran0.writeAction("slorii X16 X16 12 644")
    tran0.writeAction("movir X17 -7460")
    tran0.writeAction("slorii X17 X17 12 2613")
    tran0.writeAction("slorii X17 X17 12 769")
    tran0.writeAction("slorii X17 X17 12 1323")
    tran0.writeAction("slorii X17 X17 12 1108")
    tran0.writeAction("movir X18 -7111")
    tran0.writeAction("slorii X18 X18 12 1314")
    tran0.writeAction("slorii X18 X18 12 31")
    tran0.writeAction("slorii X18 X18 12 3493")
    tran0.writeAction("slorii X18 X18 12 2380")
    tran0.writeAction("sr X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
