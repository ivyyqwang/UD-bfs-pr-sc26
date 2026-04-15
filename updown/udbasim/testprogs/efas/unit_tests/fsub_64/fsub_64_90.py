from EFA_v2 import *
def fsub_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18318378655595664423, 10808443900464317788]
    tran0.writeAction("movir X16 65079")
    tran0.writeAction("slorii X16 X16 12 3909")
    tran0.writeAction("slorii X16 X16 12 1299")
    tran0.writeAction("slorii X16 X16 12 3593")
    tran0.writeAction("slorii X16 X16 12 1063")
    tran0.writeAction("movir X17 38399")
    tran0.writeAction("slorii X17 X17 12 1255")
    tran0.writeAction("slorii X17 X17 12 1597")
    tran0.writeAction("slorii X17 X17 12 3740")
    tran0.writeAction("slorii X17 X17 12 1372")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
