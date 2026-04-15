from EFA_v2 import *
def fadd_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7836259635778390470, 17463130467330907951]
    tran0.writeAction("movir X16 27839")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 3798")
    tran0.writeAction("slorii X16 X16 12 1240")
    tran0.writeAction("slorii X16 X16 12 2502")
    tran0.writeAction("movir X17 62041")
    tran0.writeAction("slorii X17 X17 12 2058")
    tran0.writeAction("slorii X17 X17 12 747")
    tran0.writeAction("slorii X17 X17 12 2293")
    tran0.writeAction("slorii X17 X17 12 3887")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
