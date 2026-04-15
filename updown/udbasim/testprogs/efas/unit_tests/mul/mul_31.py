from EFA_v2 import *
def mul_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1871621579817291175, 6407315748198231101]
    tran0.writeAction("movir X16 58886")
    tran0.writeAction("slorii X16 X16 12 2721")
    tran0.writeAction("slorii X16 X16 12 1765")
    tran0.writeAction("slorii X16 X16 12 143")
    tran0.writeAction("slorii X16 X16 12 601")
    tran0.writeAction("movir X17 22763")
    tran0.writeAction("slorii X17 X17 12 1467")
    tran0.writeAction("slorii X17 X17 12 2495")
    tran0.writeAction("slorii X17 X17 12 498")
    tran0.writeAction("slorii X17 X17 12 3133")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
