from EFA_v2 import *
def fdiv_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3713163408497451205, 9186714006635097301]
    tran0.writeAction("movir X16 13191")
    tran0.writeAction("slorii X16 X16 12 3303")
    tran0.writeAction("slorii X16 X16 12 612")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("movir X17 32637")
    tran0.writeAction("slorii X17 X17 12 3131")
    tran0.writeAction("slorii X17 X17 12 1850")
    tran0.writeAction("slorii X17 X17 12 2418")
    tran0.writeAction("slorii X17 X17 12 3285")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
