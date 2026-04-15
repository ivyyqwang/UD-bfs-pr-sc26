from EFA_v2 import *
def sri_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 31192")
    tran0.writeAction("slorii X16 X16 12 95")
    tran0.writeAction("slorii X16 X16 12 794")
    tran0.writeAction("slorii X16 X16 12 571")
    tran0.writeAction("slorii X16 X16 12 1915")
    tran0.writeAction("movir X17 -6392")
    tran0.writeAction("slorii X17 X17 12 3856")
    tran0.writeAction("slorii X17 X17 12 1483")
    tran0.writeAction("slorii X17 X17 12 1350")
    tran0.writeAction("slorii X17 X17 12 3674")
    tran0.writeAction("sri X16 X17 18")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
