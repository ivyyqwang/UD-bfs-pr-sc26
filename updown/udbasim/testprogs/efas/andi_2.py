from EFA_v2 import *
def andi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -3483")
    tran0.writeAction("slorii X16 X16 12 333")
    tran0.writeAction("slorii X16 X16 12 2610")
    tran0.writeAction("slorii X16 X16 12 1259")
    tran0.writeAction("slorii X16 X16 12 2858")
    tran0.writeAction("movir X17 6942")
    tran0.writeAction("slorii X17 X17 12 2552")
    tran0.writeAction("slorii X17 X17 12 1023")
    tran0.writeAction("slorii X17 X17 12 1361")
    tran0.writeAction("slorii X17 X17 12 2092")
    tran0.writeAction("andi X16 X17 -27256")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
