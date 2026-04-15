from EFA_v2 import *
def srori_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -22833")
    tran0.writeAction("slorii X16 X16 12 3295")
    tran0.writeAction("slorii X16 X16 12 690")
    tran0.writeAction("slorii X16 X16 12 3139")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("movir X17 -18660")
    tran0.writeAction("slorii X17 X17 12 1281")
    tran0.writeAction("slorii X17 X17 12 153")
    tran0.writeAction("slorii X17 X17 12 3055")
    tran0.writeAction("slorii X17 X17 12 1022")
    tran0.writeAction("srori X16 X17 13")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
