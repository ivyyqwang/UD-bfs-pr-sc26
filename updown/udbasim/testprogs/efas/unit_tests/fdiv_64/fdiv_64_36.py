from EFA_v2 import *
def fdiv_64_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13591538441360079983, 2910441495095485654]
    tran0.writeAction("movir X16 48286")
    tran0.writeAction("slorii X16 X16 12 3459")
    tran0.writeAction("slorii X16 X16 12 908")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("slorii X16 X16 12 3183")
    tran0.writeAction("movir X17 10339")
    tran0.writeAction("slorii X17 X17 12 3953")
    tran0.writeAction("slorii X17 X17 12 3742")
    tran0.writeAction("slorii X17 X17 12 2962")
    tran0.writeAction("slorii X17 X17 12 1238")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
