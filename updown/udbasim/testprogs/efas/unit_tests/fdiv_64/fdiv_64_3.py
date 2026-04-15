from EFA_v2 import *
def fdiv_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18432934374733924864, 14823682265863581246]
    tran0.writeAction("movir X16 65486")
    tran0.writeAction("slorii X16 X16 12 3842")
    tran0.writeAction("slorii X16 X16 12 1766")
    tran0.writeAction("slorii X16 X16 12 420")
    tran0.writeAction("slorii X16 X16 12 2560")
    tran0.writeAction("movir X17 52664")
    tran0.writeAction("slorii X17 X17 12 1223")
    tran0.writeAction("slorii X17 X17 12 2888")
    tran0.writeAction("slorii X17 X17 12 230")
    tran0.writeAction("slorii X17 X17 12 3646")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
