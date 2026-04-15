from EFA_v2 import *
def andi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 23329")
    tran0.writeAction("slorii X16 X16 12 765")
    tran0.writeAction("slorii X16 X16 12 807")
    tran0.writeAction("slorii X16 X16 12 3647")
    tran0.writeAction("slorii X16 X16 12 677")
    tran0.writeAction("movir X17 978")
    tran0.writeAction("slorii X17 X17 12 253")
    tran0.writeAction("slorii X17 X17 12 355")
    tran0.writeAction("slorii X17 X17 12 840")
    tran0.writeAction("slorii X17 X17 12 567")
    tran0.writeAction("andi X16 X17 -2350")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
