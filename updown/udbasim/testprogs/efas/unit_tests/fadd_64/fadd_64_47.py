from EFA_v2 import *
def fadd_64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12166835232497767874, 2137236089575273758]
    tran0.writeAction("movir X16 43225")
    tran0.writeAction("slorii X16 X16 12 1154")
    tran0.writeAction("slorii X16 X16 12 3689")
    tran0.writeAction("slorii X16 X16 12 3017")
    tran0.writeAction("slorii X16 X16 12 1474")
    tran0.writeAction("movir X17 7592")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("slorii X17 X17 12 1632")
    tran0.writeAction("slorii X17 X17 12 1143")
    tran0.writeAction("slorii X17 X17 12 1310")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
