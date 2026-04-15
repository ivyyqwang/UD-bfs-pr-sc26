from EFA_v2 import *
def fsub_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1646511054353853140, 16230908246991010279]
    tran0.writeAction("movir X16 5849")
    tran0.writeAction("slorii X16 X16 12 2385")
    tran0.writeAction("slorii X16 X16 12 1169")
    tran0.writeAction("slorii X16 X16 12 2110")
    tran0.writeAction("slorii X16 X16 12 2772")
    tran0.writeAction("movir X17 57663")
    tran0.writeAction("slorii X17 X17 12 3152")
    tran0.writeAction("slorii X17 X17 12 3643")
    tran0.writeAction("slorii X17 X17 12 3511")
    tran0.writeAction("slorii X17 X17 12 2535")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
