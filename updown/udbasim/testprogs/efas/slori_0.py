from EFA_v2 import *
def slori_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -20449")
    tran0.writeAction("slorii X16 X16 12 355")
    tran0.writeAction("slorii X16 X16 12 1239")
    tran0.writeAction("slorii X16 X16 12 3938")
    tran0.writeAction("slorii X16 X16 12 3186")
    tran0.writeAction("movir X17 -1487")
    tran0.writeAction("slorii X17 X17 12 124")
    tran0.writeAction("slorii X17 X17 12 2241")
    tran0.writeAction("slorii X17 X17 12 2263")
    tran0.writeAction("slorii X17 X17 12 2610")
    tran0.writeAction("slori X16 X17 36")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
