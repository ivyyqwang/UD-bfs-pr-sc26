from EFA_v2 import *
def fmul_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16656898801335426879, 7408952989973312067]
    tran0.writeAction("movir X16 59177")
    tran0.writeAction("slorii X16 X16 12 787")
    tran0.writeAction("slorii X16 X16 12 1329")
    tran0.writeAction("slorii X16 X16 12 933")
    tran0.writeAction("slorii X16 X16 12 3903")
    tran0.writeAction("movir X17 26321")
    tran0.writeAction("slorii X17 X17 12 3639")
    tran0.writeAction("slorii X17 X17 12 3444")
    tran0.writeAction("slorii X17 X17 12 3799")
    tran0.writeAction("slorii X17 X17 12 579")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
