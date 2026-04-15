from EFA_v2 import *
def srori_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -23322")
    tran0.writeAction("slorii X16 X16 12 2131")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 782")
    tran0.writeAction("slorii X16 X16 12 2526")
    tran0.writeAction("movir X17 29379")
    tran0.writeAction("slorii X17 X17 12 2037")
    tran0.writeAction("slorii X17 X17 12 278")
    tran0.writeAction("slorii X17 X17 12 3169")
    tran0.writeAction("slorii X17 X17 12 422")
    tran0.writeAction("srori X16 X17 20")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
