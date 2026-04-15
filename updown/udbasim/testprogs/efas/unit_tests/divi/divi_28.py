from EFA_v2 import *
def divi_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5336298049490266673, 3213]
    tran0.writeAction("movir X16 46577")
    tran0.writeAction("slorii X16 X16 12 2707")
    tran0.writeAction("slorii X16 X16 12 616")
    tran0.writeAction("slorii X16 X16 12 2141")
    tran0.writeAction("slorii X16 X16 12 1487")
    tran0.writeAction("divi X16 X17 3213")
    tran0.writeAction("yieldt")
    return efa
