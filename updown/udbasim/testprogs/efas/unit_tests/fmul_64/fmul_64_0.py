from EFA_v2 import *
def fmul_64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18358709277278524546, 8776797939075774284]
    tran0.writeAction("movir X16 65223")
    tran0.writeAction("slorii X16 X16 12 973")
    tran0.writeAction("slorii X16 X16 12 430")
    tran0.writeAction("slorii X16 X16 12 3501")
    tran0.writeAction("slorii X16 X16 12 1154")
    tran0.writeAction("movir X17 31181")
    tran0.writeAction("slorii X17 X17 12 1843")
    tran0.writeAction("slorii X17 X17 12 2399")
    tran0.writeAction("slorii X17 X17 12 4063")
    tran0.writeAction("slorii X17 X17 12 1868")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
