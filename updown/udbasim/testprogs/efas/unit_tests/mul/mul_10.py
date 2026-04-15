from EFA_v2 import *
def mul_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5949534373677673578, -1461755530056277013]
    tran0.writeAction("movir X16 44399")
    tran0.writeAction("slorii X16 X16 12 32")
    tran0.writeAction("slorii X16 X16 12 597")
    tran0.writeAction("slorii X16 X16 12 3957")
    tran0.writeAction("slorii X16 X16 12 918")
    tran0.writeAction("movir X17 60342")
    tran0.writeAction("slorii X17 X17 12 3281")
    tran0.writeAction("slorii X17 X17 12 1810")
    tran0.writeAction("slorii X17 X17 12 2182")
    tran0.writeAction("slorii X17 X17 12 1003")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
