from EFA_v2 import *
def fadd_64_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11451484104490102443, 12764188605302609291]
    tran0.writeAction("movir X16 40683")
    tran0.writeAction("slorii X16 X16 12 3457")
    tran0.writeAction("slorii X16 X16 12 3799")
    tran0.writeAction("slorii X16 X16 12 674")
    tran0.writeAction("slorii X16 X16 12 3755")
    tran0.writeAction("movir X17 45347")
    tran0.writeAction("slorii X17 X17 12 2078")
    tran0.writeAction("slorii X17 X17 12 2225")
    tran0.writeAction("slorii X17 X17 12 617")
    tran0.writeAction("slorii X17 X17 12 1419")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
