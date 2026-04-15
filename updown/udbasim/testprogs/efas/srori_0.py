from EFA_v2 import *
def srori_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 1466")
    tran0.writeAction("slorii X16 X16 12 3018")
    tran0.writeAction("slorii X16 X16 12 2206")
    tran0.writeAction("slorii X16 X16 12 1986")
    tran0.writeAction("slorii X16 X16 12 50")
    tran0.writeAction("movir X17 -8488")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("slorii X17 X17 12 3951")
    tran0.writeAction("slorii X17 X17 12 2626")
    tran0.writeAction("slorii X17 X17 12 1326")
    tran0.writeAction("srori X16 X17 7")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
