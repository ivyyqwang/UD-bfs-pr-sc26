from EFA_v2 import *
def sub_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5611119064923366979, -6341260642581381681]
    tran0.writeAction("movir X16 19934")
    tran0.writeAction("slorii X16 X16 12 2864")
    tran0.writeAction("slorii X16 X16 12 3969")
    tran0.writeAction("slorii X16 X16 12 734")
    tran0.writeAction("slorii X16 X16 12 1603")
    tran0.writeAction("movir X17 43007")
    tran0.writeAction("slorii X17 X17 12 1296")
    tran0.writeAction("slorii X17 X17 12 2818")
    tran0.writeAction("slorii X17 X17 12 3159")
    tran0.writeAction("slorii X17 X17 12 3535")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
