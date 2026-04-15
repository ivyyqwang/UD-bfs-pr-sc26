from EFA_v2 import *
def mod_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1027141836377028685, 876554202739435729]
    tran0.writeAction("movir X16 3649")
    tran0.writeAction("slorii X16 X16 12 576")
    tran0.writeAction("slorii X16 X16 12 3811")
    tran0.writeAction("slorii X16 X16 12 799")
    tran0.writeAction("slorii X16 X16 12 2125")
    tran0.writeAction("movir X17 3114")
    tran0.writeAction("slorii X17 X17 12 598")
    tran0.writeAction("slorii X17 X17 12 1848")
    tran0.writeAction("slorii X17 X17 12 2702")
    tran0.writeAction("slorii X17 X17 12 2257")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
