from EFA_v2 import *
def sub_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6829574917708201651, -4470339893458235013]
    tran0.writeAction("movir X16 24263")
    tran0.writeAction("slorii X16 X16 12 2147")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("slorii X16 X16 12 3747")
    tran0.writeAction("slorii X16 X16 12 3763")
    tran0.writeAction("movir X17 49654")
    tran0.writeAction("slorii X17 X17 12 664")
    tran0.writeAction("slorii X17 X17 12 3393")
    tran0.writeAction("slorii X17 X17 12 673")
    tran0.writeAction("slorii X17 X17 12 379")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
