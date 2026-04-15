from EFA_v2 import *
def div_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [882202056744849860, 589637372743288999]
    tran0.writeAction("movir X16 3134")
    tran0.writeAction("slorii X16 X16 12 865")
    tran0.writeAction("slorii X16 X16 12 2228")
    tran0.writeAction("slorii X16 X16 12 1621")
    tran0.writeAction("slorii X16 X16 12 452")
    tran0.writeAction("movir X17 2094")
    tran0.writeAction("slorii X17 X17 12 3329")
    tran0.writeAction("slorii X17 X17 12 260")
    tran0.writeAction("slorii X17 X17 12 2696")
    tran0.writeAction("slorii X17 X17 12 2215")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
