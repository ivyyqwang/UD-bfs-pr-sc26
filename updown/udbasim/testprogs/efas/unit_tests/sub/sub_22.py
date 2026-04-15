from EFA_v2 import *
def sub_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1035054594520793587, 8435792269171491395]
    tran0.writeAction("movir X16 3677")
    tran0.writeAction("slorii X16 X16 12 1034")
    tran0.writeAction("slorii X16 X16 12 2933")
    tran0.writeAction("slorii X16 X16 12 2244")
    tran0.writeAction("slorii X16 X16 12 499")
    tran0.writeAction("movir X17 29969")
    tran0.writeAction("slorii X17 X17 12 3909")
    tran0.writeAction("slorii X17 X17 12 4034")
    tran0.writeAction("slorii X17 X17 12 3904")
    tran0.writeAction("slorii X17 X17 12 579")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
