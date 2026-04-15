from EFA_v2 import *
def fdiv_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14736333285183565984, 3573096140599836941]
    tran0.writeAction("movir X16 52353")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("slorii X16 X16 12 3043")
    tran0.writeAction("slorii X16 X16 12 539")
    tran0.writeAction("slorii X16 X16 12 160")
    tran0.writeAction("movir X17 12694")
    tran0.writeAction("slorii X17 X17 12 768")
    tran0.writeAction("slorii X17 X17 12 576")
    tran0.writeAction("slorii X17 X17 12 3164")
    tran0.writeAction("slorii X17 X17 12 269")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
