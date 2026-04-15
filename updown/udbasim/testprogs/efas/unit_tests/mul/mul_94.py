from EFA_v2 import *
def mul_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2897523124274720923, -4813538099411817718]
    tran0.writeAction("movir X16 55241")
    tran0.writeAction("slorii X16 X16 12 3809")
    tran0.writeAction("slorii X16 X16 12 505")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 3941")
    tran0.writeAction("movir X17 48434")
    tran0.writeAction("slorii X17 X17 12 3593")
    tran0.writeAction("slorii X17 X17 12 2575")
    tran0.writeAction("slorii X17 X17 12 3070")
    tran0.writeAction("slorii X17 X17 12 2826")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
