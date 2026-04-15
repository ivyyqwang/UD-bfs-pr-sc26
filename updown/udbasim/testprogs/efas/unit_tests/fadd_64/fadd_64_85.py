from EFA_v2 import *
def fadd_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18260018168024256846, 13165602032974601068]
    tran0.writeAction("movir X16 64872")
    tran0.writeAction("slorii X16 X16 12 2524")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 1085")
    tran0.writeAction("slorii X16 X16 12 334")
    tran0.writeAction("movir X17 46773")
    tran0.writeAction("slorii X17 X17 12 2516")
    tran0.writeAction("slorii X17 X17 12 2925")
    tran0.writeAction("slorii X17 X17 12 2505")
    tran0.writeAction("slorii X17 X17 12 2924")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
