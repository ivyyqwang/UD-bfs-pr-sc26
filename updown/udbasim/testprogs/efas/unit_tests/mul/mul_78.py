from EFA_v2 import *
def mul_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3112428172927451904, -4134752989678102957]
    tran0.writeAction("movir X16 11057")
    tran0.writeAction("slorii X16 X16 12 2318")
    tran0.writeAction("slorii X16 X16 12 3796")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 768")
    tran0.writeAction("movir X17 50846")
    tran0.writeAction("slorii X17 X17 12 1665")
    tran0.writeAction("slorii X17 X17 12 16")
    tran0.writeAction("slorii X17 X17 12 1033")
    tran0.writeAction("slorii X17 X17 12 1619")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
