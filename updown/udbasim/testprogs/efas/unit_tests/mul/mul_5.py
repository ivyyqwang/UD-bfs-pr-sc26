from EFA_v2 import *
def mul_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4262230324942405486, -7517769086689042191]
    tran0.writeAction("movir X16 50393")
    tran0.writeAction("slorii X16 X16 12 2113")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("slorii X16 X16 12 3728")
    tran0.writeAction("slorii X16 X16 12 146")
    tran0.writeAction("movir X17 38827")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 12 2228")
    tran0.writeAction("slorii X17 X17 12 1994")
    tran0.writeAction("slorii X17 X17 12 241")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
