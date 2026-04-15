from EFA_v2 import *
def fdiv_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3556608498, 1135509183]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 211")
    tran0.writeAction("slorii X16 X16 12 4056")
    tran0.writeAction("slorii X16 X16 12 2546")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 67")
    tran0.writeAction("slorii X17 X17 12 2791")
    tran0.writeAction("slorii X17 X17 12 3775")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
