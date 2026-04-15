from EFA_v2 import *
def mul_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5882469568807048980, 5256804971593770087]
    tran0.writeAction("movir X16 20898")
    tran0.writeAction("slorii X16 X16 12 2990")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("slorii X16 X16 12 3233")
    tran0.writeAction("slorii X16 X16 12 1812")
    tran0.writeAction("movir X17 18675")
    tran0.writeAction("slorii X17 X17 12 3780")
    tran0.writeAction("slorii X17 X17 12 1305")
    tran0.writeAction("slorii X17 X17 12 1450")
    tran0.writeAction("slorii X17 X17 12 1127")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
