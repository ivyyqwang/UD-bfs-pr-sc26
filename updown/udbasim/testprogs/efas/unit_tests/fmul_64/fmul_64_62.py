from EFA_v2 import *
def fmul_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [234771363531789296, 13358297214583211870]
    tran0.writeAction("movir X16 834")
    tran0.writeAction("slorii X16 X16 12 308")
    tran0.writeAction("slorii X16 X16 12 4014")
    tran0.writeAction("slorii X16 X16 12 3057")
    tran0.writeAction("slorii X16 X16 12 1008")
    tran0.writeAction("movir X17 47458")
    tran0.writeAction("slorii X17 X17 12 840")
    tran0.writeAction("slorii X17 X17 12 2711")
    tran0.writeAction("slorii X17 X17 12 1320")
    tran0.writeAction("slorii X17 X17 12 1886")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
