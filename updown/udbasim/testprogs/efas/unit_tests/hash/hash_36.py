from EFA_v2 import *
def hash_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9210302560921764251, -6017095718098589136]
    tran0.writeAction("movir X16 32721")
    tran0.writeAction("slorii X16 X16 12 2326")
    tran0.writeAction("slorii X16 X16 12 385")
    tran0.writeAction("slorii X16 X16 12 2508")
    tran0.writeAction("slorii X16 X16 12 411")
    tran0.writeAction("movir X17 44158")
    tran0.writeAction("slorii X17 X17 12 4021")
    tran0.writeAction("slorii X17 X17 12 775")
    tran0.writeAction("slorii X17 X17 12 858")
    tran0.writeAction("slorii X17 X17 12 2608")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
