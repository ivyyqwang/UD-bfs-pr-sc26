from EFA_v2 import *
def fadd_64_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18070833911948792572, 7168641419464591552]
    tran0.writeAction("movir X16 64200")
    tran0.writeAction("slorii X16 X16 12 2043")
    tran0.writeAction("slorii X16 X16 12 788")
    tran0.writeAction("slorii X16 X16 12 3237")
    tran0.writeAction("slorii X16 X16 12 764")
    tran0.writeAction("movir X17 25468")
    tran0.writeAction("slorii X17 X17 12 534")
    tran0.writeAction("slorii X17 X17 12 977")
    tran0.writeAction("slorii X17 X17 12 1388")
    tran0.writeAction("slorii X17 X17 12 2240")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
