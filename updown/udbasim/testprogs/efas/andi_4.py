from EFA_v2 import *
def andi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -2257")
    tran0.writeAction("slorii X16 X16 12 2272")
    tran0.writeAction("slorii X16 X16 12 1808")
    tran0.writeAction("slorii X16 X16 12 2508")
    tran0.writeAction("slorii X16 X16 12 3766")
    tran0.writeAction("movir X17 -16658")
    tran0.writeAction("slorii X17 X17 12 3398")
    tran0.writeAction("slorii X17 X17 12 3609")
    tran0.writeAction("slorii X17 X17 12 515")
    tran0.writeAction("slorii X17 X17 12 2736")
    tran0.writeAction("andi X16 X17 1307")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
