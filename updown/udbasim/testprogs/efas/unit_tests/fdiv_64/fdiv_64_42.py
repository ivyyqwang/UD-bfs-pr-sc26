from EFA_v2 import *
def fdiv_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16224805268115136493, 2930131703880283515]
    tran0.writeAction("movir X16 57642")
    tran0.writeAction("slorii X16 X16 12 358")
    tran0.writeAction("slorii X16 X16 12 3515")
    tran0.writeAction("slorii X16 X16 12 3641")
    tran0.writeAction("slorii X16 X16 12 4077")
    tran0.writeAction("movir X17 10409")
    tran0.writeAction("slorii X17 X17 12 3764")
    tran0.writeAction("slorii X17 X17 12 666")
    tran0.writeAction("slorii X17 X17 12 3663")
    tran0.writeAction("slorii X17 X17 12 1403")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
