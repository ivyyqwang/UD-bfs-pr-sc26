from EFA_v2 import *
def sub_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8197268704724719118, -4946126622457676033]
    tran0.writeAction("movir X16 36413")
    tran0.writeAction("slorii X16 X16 12 1848")
    tran0.writeAction("slorii X16 X16 12 2886")
    tran0.writeAction("slorii X16 X16 12 1870")
    tran0.writeAction("slorii X16 X16 12 2546")
    tran0.writeAction("movir X17 47963")
    tran0.writeAction("slorii X17 X17 12 3392")
    tran0.writeAction("slorii X17 X17 12 2790")
    tran0.writeAction("slorii X17 X17 12 1259")
    tran0.writeAction("slorii X17 X17 12 3839")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
