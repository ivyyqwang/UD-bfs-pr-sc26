from EFA_v2 import *
def mod_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2273780388437251626, 3809416385573460529]
    tran0.writeAction("movir X16 57457")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("slorii X16 X16 12 2209")
    tran0.writeAction("slorii X16 X16 12 3882")
    tran0.writeAction("slorii X16 X16 12 2518")
    tran0.writeAction("movir X17 13533")
    tran0.writeAction("slorii X17 X17 12 3136")
    tran0.writeAction("slorii X17 X17 12 1279")
    tran0.writeAction("slorii X17 X17 12 2697")
    tran0.writeAction("slorii X17 X17 12 2609")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
