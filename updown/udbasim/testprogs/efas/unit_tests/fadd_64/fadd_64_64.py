from EFA_v2 import *
def fadd_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [589199052886497548, 12921136390947655794]
    tran0.writeAction("movir X16 2093")
    tran0.writeAction("slorii X16 X16 12 1046")
    tran0.writeAction("slorii X16 X16 12 2745")
    tran0.writeAction("slorii X16 X16 12 1213")
    tran0.writeAction("slorii X16 X16 12 2316")
    tran0.writeAction("movir X17 45905")
    tran0.writeAction("slorii X17 X17 12 401")
    tran0.writeAction("slorii X17 X17 12 1700")
    tran0.writeAction("slorii X17 X17 12 3309")
    tran0.writeAction("slorii X17 X17 12 114")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
