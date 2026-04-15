from EFA_v2 import *
def fdiv_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5556336738436535098, 6476464173999692267]
    tran0.writeAction("movir X16 19740")
    tran0.writeAction("slorii X16 X16 12 301")
    tran0.writeAction("slorii X16 X16 12 810")
    tran0.writeAction("slorii X16 X16 12 3941")
    tran0.writeAction("slorii X16 X16 12 826")
    tran0.writeAction("movir X17 23009")
    tran0.writeAction("slorii X17 X17 12 93")
    tran0.writeAction("slorii X17 X17 12 2619")
    tran0.writeAction("slorii X17 X17 12 3257")
    tran0.writeAction("slorii X17 X17 12 2539")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
