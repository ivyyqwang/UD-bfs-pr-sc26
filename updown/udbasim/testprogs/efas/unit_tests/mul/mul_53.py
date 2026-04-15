from EFA_v2 import *
def mul_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2454059335384066680, -7297164404359992743]
    tran0.writeAction("movir X16 8718")
    tran0.writeAction("slorii X16 X16 12 2335")
    tran0.writeAction("slorii X16 X16 12 1695")
    tran0.writeAction("slorii X16 X16 12 1222")
    tran0.writeAction("slorii X16 X16 12 2680")
    tran0.writeAction("movir X17 39611")
    tran0.writeAction("slorii X17 X17 12 1082")
    tran0.writeAction("slorii X17 X17 12 738")
    tran0.writeAction("slorii X17 X17 12 2038")
    tran0.writeAction("slorii X17 X17 12 2649")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
