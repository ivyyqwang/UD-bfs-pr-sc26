from EFA_v2 import *
def mul_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5404226905289551964, 1073779212695791067]
    tran0.writeAction("movir X16 19199")
    tran0.writeAction("slorii X16 X16 12 2747")
    tran0.writeAction("slorii X16 X16 12 3279")
    tran0.writeAction("slorii X16 X16 12 1607")
    tran0.writeAction("slorii X16 X16 12 92")
    tran0.writeAction("movir X17 3814")
    tran0.writeAction("slorii X17 X17 12 3400")
    tran0.writeAction("slorii X17 X17 12 315")
    tran0.writeAction("slorii X17 X17 12 3814")
    tran0.writeAction("slorii X17 X17 12 1499")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
