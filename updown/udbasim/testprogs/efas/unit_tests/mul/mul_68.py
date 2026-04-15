from EFA_v2 import *
def mul_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4908475994553016563, 1173906217104661634]
    tran0.writeAction("movir X16 17438")
    tran0.writeAction("slorii X16 X16 12 1678")
    tran0.writeAction("slorii X16 X16 12 2347")
    tran0.writeAction("slorii X16 X16 12 3542")
    tran0.writeAction("slorii X16 X16 12 243")
    tran0.writeAction("movir X17 4170")
    tran0.writeAction("slorii X17 X17 12 2263")
    tran0.writeAction("slorii X17 X17 12 3102")
    tran0.writeAction("slorii X17 X17 12 597")
    tran0.writeAction("slorii X17 X17 12 3202")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
