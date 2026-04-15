from EFA_v2 import *
def fdiv_32_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3332122529, 2176493185]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 198")
    tran0.writeAction("slorii X16 X16 12 2498")
    tran0.writeAction("slorii X16 X16 12 1953")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 129")
    tran0.writeAction("slorii X17 X17 12 2986")
    tran0.writeAction("slorii X17 X17 12 1665")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
