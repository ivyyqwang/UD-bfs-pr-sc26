from EFA_v2 import *
def mul_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3310024938017903464, -8324872345330099437]
    tran0.writeAction("movir X16 11759")
    tran0.writeAction("slorii X16 X16 12 2338")
    tran0.writeAction("slorii X16 X16 12 1236")
    tran0.writeAction("slorii X16 X16 12 989")
    tran0.writeAction("slorii X16 X16 12 872")
    tran0.writeAction("movir X17 35960")
    tran0.writeAction("slorii X17 X17 12 459")
    tran0.writeAction("slorii X17 X17 12 1408")
    tran0.writeAction("slorii X17 X17 12 517")
    tran0.writeAction("slorii X17 X17 12 2835")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
