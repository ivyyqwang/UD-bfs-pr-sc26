from EFA_v2 import *
def mul_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2900689454240916444, -5842307546563614526]
    tran0.writeAction("movir X16 55230")
    tran0.writeAction("slorii X16 X16 12 2788")
    tran0.writeAction("slorii X16 X16 12 3924")
    tran0.writeAction("slorii X16 X16 12 1017")
    tran0.writeAction("slorii X16 X16 12 3108")
    tran0.writeAction("movir X17 44779")
    tran0.writeAction("slorii X17 X17 12 3907")
    tran0.writeAction("slorii X17 X17 12 3458")
    tran0.writeAction("slorii X17 X17 12 2014")
    tran0.writeAction("slorii X17 X17 12 2242")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
