from EFA_v2 import *
def fdiv_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3834011024628227846, 111665682800616770]
    tran0.writeAction("movir X16 13621")
    tran0.writeAction("slorii X16 X16 12 587")
    tran0.writeAction("slorii X16 X16 12 1699")
    tran0.writeAction("slorii X16 X16 12 3673")
    tran0.writeAction("slorii X16 X16 12 3846")
    tran0.writeAction("movir X17 396")
    tran0.writeAction("slorii X17 X17 12 2933")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 12 3818")
    tran0.writeAction("slorii X17 X17 12 1346")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
