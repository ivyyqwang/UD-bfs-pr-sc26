from EFA_v2 import *
def fadd_32_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3620624071, 436755579]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 215")
    tran0.writeAction("slorii X16 X16 12 3301")
    tran0.writeAction("slorii X16 X16 12 1735")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 26")
    tran0.writeAction("slorii X17 X17 12 133")
    tran0.writeAction("slorii X17 X17 12 3195")
    tran0.writeAction("fadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
