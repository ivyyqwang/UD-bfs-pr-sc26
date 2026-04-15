from EFA_v2 import *
def fadd_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3418444242141456083, 15434078695471938270]
    tran0.writeAction("movir X16 12144")
    tran0.writeAction("slorii X16 X16 12 3086")
    tran0.writeAction("slorii X16 X16 12 3377")
    tran0.writeAction("slorii X16 X16 12 1314")
    tran0.writeAction("slorii X16 X16 12 1747")
    tran0.writeAction("movir X17 54832")
    tran0.writeAction("slorii X17 X17 12 3532")
    tran0.writeAction("slorii X17 X17 12 3295")
    tran0.writeAction("slorii X17 X17 12 119")
    tran0.writeAction("slorii X17 X17 12 2782")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
