from EFA_v2 import *
def srori_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 6368")
    tran0.writeAction("slorii X16 X16 12 2836")
    tran0.writeAction("slorii X16 X16 12 1552")
    tran0.writeAction("slorii X16 X16 12 3099")
    tran0.writeAction("slorii X16 X16 12 2507")
    tran0.writeAction("movir X17 -21199")
    tran0.writeAction("slorii X17 X17 12 665")
    tran0.writeAction("slorii X17 X17 12 34")
    tran0.writeAction("slorii X17 X17 12 452")
    tran0.writeAction("slorii X17 X17 12 3970")
    tran0.writeAction("srori X16 X17 21")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
