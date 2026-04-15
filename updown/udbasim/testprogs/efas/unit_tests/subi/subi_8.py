from EFA_v2 import *
def subi_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5555316069159258615, -18326]
    tran0.writeAction("movir X16 45799")
    tran0.writeAction("slorii X16 X16 12 2263")
    tran0.writeAction("slorii X16 X16 12 2026")
    tran0.writeAction("slorii X16 X16 12 3043")
    tran0.writeAction("slorii X16 X16 12 1545")
    tran0.writeAction("subi X16 X17 -18326")
    tran0.writeAction("yieldt")
    return efa
