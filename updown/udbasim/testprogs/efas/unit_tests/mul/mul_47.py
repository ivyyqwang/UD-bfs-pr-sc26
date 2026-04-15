from EFA_v2 import *
def mul_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4539103526354426907, 7711820168720708871]
    tran0.writeAction("movir X16 16126")
    tran0.writeAction("slorii X16 X16 12 553")
    tran0.writeAction("slorii X16 X16 12 2983")
    tran0.writeAction("slorii X16 X16 12 321")
    tran0.writeAction("slorii X16 X16 12 3099")
    tran0.writeAction("movir X17 27397")
    tran0.writeAction("slorii X17 X17 12 3641")
    tran0.writeAction("slorii X17 X17 12 1440")
    tran0.writeAction("slorii X17 X17 12 1191")
    tran0.writeAction("slorii X17 X17 12 1287")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
