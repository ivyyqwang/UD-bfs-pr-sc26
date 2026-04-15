from EFA_v2 import *
def sub_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5767587451581313893, 7509866104305908299]
    tran0.writeAction("movir X16 20490")
    tran0.writeAction("slorii X16 X16 12 2403")
    tran0.writeAction("slorii X16 X16 12 2734")
    tran0.writeAction("slorii X16 X16 12 2067")
    tran0.writeAction("slorii X16 X16 12 869")
    tran0.writeAction("movir X17 26680")
    tran0.writeAction("slorii X17 X17 12 1654")
    tran0.writeAction("slorii X17 X17 12 3793")
    tran0.writeAction("slorii X17 X17 12 3687")
    tran0.writeAction("slorii X17 X17 12 2635")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
