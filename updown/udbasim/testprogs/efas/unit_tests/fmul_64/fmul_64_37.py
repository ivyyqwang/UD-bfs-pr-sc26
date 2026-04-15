from EFA_v2 import *
def fmul_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15398958469987636211, 15836036182055710525]
    tran0.writeAction("movir X16 54708")
    tran0.writeAction("slorii X16 X16 12 370")
    tran0.writeAction("slorii X16 X16 12 1066")
    tran0.writeAction("slorii X16 X16 12 2481")
    tran0.writeAction("slorii X16 X16 12 1011")
    tran0.writeAction("movir X17 56260")
    tran0.writeAction("slorii X17 X17 12 3696")
    tran0.writeAction("slorii X17 X17 12 305")
    tran0.writeAction("slorii X17 X17 12 2718")
    tran0.writeAction("slorii X17 X17 12 3901")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
