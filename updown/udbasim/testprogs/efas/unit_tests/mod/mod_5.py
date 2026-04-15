from EFA_v2 import *
def mod_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7479609213472853613, 2850065803261639711]
    tran0.writeAction("movir X16 26572")
    tran0.writeAction("slorii X16 X16 12 3727")
    tran0.writeAction("slorii X16 X16 12 883")
    tran0.writeAction("slorii X16 X16 12 3228")
    tran0.writeAction("slorii X16 X16 12 3693")
    tran0.writeAction("movir X17 10125")
    tran0.writeAction("slorii X17 X17 12 1915")
    tran0.writeAction("slorii X17 X17 12 3949")
    tran0.writeAction("slorii X17 X17 12 3679")
    tran0.writeAction("slorii X17 X17 12 3103")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
