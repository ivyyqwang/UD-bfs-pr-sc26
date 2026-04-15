from EFA_v2 import *
def hash_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6311460056081799488, -694042830283958360]
    tran0.writeAction("movir X16 43113")
    tran0.writeAction("slorii X16 X16 12 776")
    tran0.writeAction("slorii X16 X16 12 1215")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("slorii X16 X16 12 1728")
    tran0.writeAction("movir X17 63070")
    tran0.writeAction("slorii X17 X17 12 1083")
    tran0.writeAction("slorii X17 X17 12 2330")
    tran0.writeAction("slorii X17 X17 12 73")
    tran0.writeAction("slorii X17 X17 12 1960")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
