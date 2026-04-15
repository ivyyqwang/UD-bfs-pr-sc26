from EFA_v2 import *
def hash_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9203046833936259087, -4531299111464553502]
    tran0.writeAction("movir X16 32695")
    tran0.writeAction("slorii X16 X16 12 3237")
    tran0.writeAction("slorii X16 X16 12 1516")
    tran0.writeAction("slorii X16 X16 12 221")
    tran0.writeAction("slorii X16 X16 12 2063")
    tran0.writeAction("movir X17 49437")
    tran0.writeAction("slorii X17 X17 12 2423")
    tran0.writeAction("slorii X17 X17 12 1866")
    tran0.writeAction("slorii X17 X17 12 459")
    tran0.writeAction("slorii X17 X17 12 994")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
