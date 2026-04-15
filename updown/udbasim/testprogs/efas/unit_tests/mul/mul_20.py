from EFA_v2 import *
def mul_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-567836496013276365, 5257511652267467505]
    tran0.writeAction("movir X16 63518")
    tran0.writeAction("slorii X16 X16 12 2619")
    tran0.writeAction("slorii X16 X16 12 1828")
    tran0.writeAction("slorii X16 X16 12 2564")
    tran0.writeAction("slorii X16 X16 12 2867")
    tran0.writeAction("movir X17 18678")
    tran0.writeAction("slorii X17 X17 12 1775")
    tran0.writeAction("slorii X17 X17 12 3587")
    tran0.writeAction("slorii X17 X17 12 3602")
    tran0.writeAction("slorii X17 X17 12 753")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
