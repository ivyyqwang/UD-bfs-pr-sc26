from EFA_v2 import *
def hash_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3980063796305330523, 6313508462061835903]
    tran0.writeAction("movir X16 51395")
    tran0.writeAction("slorii X16 X16 12 3985")
    tran0.writeAction("slorii X16 X16 12 133")
    tran0.writeAction("slorii X16 X16 12 3391")
    tran0.writeAction("slorii X16 X16 12 3749")
    tran0.writeAction("movir X17 22430")
    tran0.writeAction("slorii X17 X17 12 359")
    tran0.writeAction("slorii X17 X17 12 3823")
    tran0.writeAction("slorii X17 X17 12 2533")
    tran0.writeAction("slorii X17 X17 12 1663")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
