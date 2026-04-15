from EFA_v2 import *
def sub_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6973613175279427490, -6587169201670122399]
    tran0.writeAction("movir X16 24775")
    tran0.writeAction("slorii X16 X16 12 1027")
    tran0.writeAction("slorii X16 X16 12 3121")
    tran0.writeAction("slorii X16 X16 12 2105")
    tran0.writeAction("slorii X16 X16 12 4002")
    tran0.writeAction("movir X17 42133")
    tran0.writeAction("slorii X17 X17 12 2760")
    tran0.writeAction("slorii X17 X17 12 747")
    tran0.writeAction("slorii X17 X17 12 241")
    tran0.writeAction("slorii X17 X17 12 1121")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
