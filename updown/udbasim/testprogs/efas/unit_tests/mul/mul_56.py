from EFA_v2 import *
def mul_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3876639796674540607, 2934735772217726767]
    tran0.writeAction("movir X16 51763")
    tran0.writeAction("slorii X16 X16 12 1674")
    tran0.writeAction("slorii X16 X16 12 1261")
    tran0.writeAction("slorii X16 X16 12 292")
    tran0.writeAction("slorii X16 X16 12 3009")
    tran0.writeAction("movir X17 10426")
    tran0.writeAction("slorii X17 X17 12 1130")
    tran0.writeAction("slorii X17 X17 12 716")
    tran0.writeAction("slorii X17 X17 12 2741")
    tran0.writeAction("slorii X17 X17 12 1839")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
