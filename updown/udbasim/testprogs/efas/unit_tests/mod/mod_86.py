from EFA_v2 import *
def mod_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4121946457558136598, -346738283570576420]
    tran0.writeAction("movir X16 14644")
    tran0.writeAction("slorii X16 X16 12 391")
    tran0.writeAction("slorii X16 X16 12 1745")
    tran0.writeAction("slorii X16 X16 12 3819")
    tran0.writeAction("slorii X16 X16 12 1814")
    tran0.writeAction("movir X17 64304")
    tran0.writeAction("slorii X17 X17 12 565")
    tran0.writeAction("slorii X17 X17 12 3649")
    tran0.writeAction("slorii X17 X17 12 3060")
    tran0.writeAction("slorii X17 X17 12 988")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
