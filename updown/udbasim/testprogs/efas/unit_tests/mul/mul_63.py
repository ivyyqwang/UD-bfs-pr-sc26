from EFA_v2 import *
def mul_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8628223014371707441, -6270007866869512767]
    tran0.writeAction("movir X16 34882")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("slorii X16 X16 12 505")
    tran0.writeAction("slorii X16 X16 12 2147")
    tran0.writeAction("slorii X16 X16 12 1487")
    tran0.writeAction("movir X17 43260")
    tran0.writeAction("slorii X17 X17 12 1873")
    tran0.writeAction("slorii X17 X17 12 164")
    tran0.writeAction("slorii X17 X17 12 1384")
    tran0.writeAction("slorii X17 X17 12 1473")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
