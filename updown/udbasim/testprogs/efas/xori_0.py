from EFA_v2 import *
def xori_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 1792")
    tran0.writeAction("slorii X16 X16 12 3227")
    tran0.writeAction("slorii X16 X16 12 3216")
    tran0.writeAction("slorii X16 X16 12 442")
    tran0.writeAction("slorii X16 X16 12 2171")
    tran0.writeAction("movir X17 5068")
    tran0.writeAction("slorii X17 X17 12 3670")
    tran0.writeAction("slorii X17 X17 12 3909")
    tran0.writeAction("slorii X17 X17 12 3259")
    tran0.writeAction("slorii X17 X17 12 373")
    tran0.writeAction("xori X16 X17 -8773")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
