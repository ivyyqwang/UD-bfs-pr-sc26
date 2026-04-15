from EFA_v2 import *
def xori_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 12949")
    tran0.writeAction("slorii X16 X16 12 136")
    tran0.writeAction("slorii X16 X16 12 2326")
    tran0.writeAction("slorii X16 X16 12 2370")
    tran0.writeAction("slorii X16 X16 12 1936")
    tran0.writeAction("movir X17 -14072")
    tran0.writeAction("slorii X17 X17 12 1436")
    tran0.writeAction("slorii X17 X17 12 3503")
    tran0.writeAction("slorii X17 X17 12 462")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("xori X16 X17 -23582")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
