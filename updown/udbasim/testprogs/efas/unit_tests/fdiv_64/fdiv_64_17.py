from EFA_v2 import *
def fdiv_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11241594007404963445, 547936746589481593]
    tran0.writeAction("movir X16 39938")
    tran0.writeAction("slorii X16 X16 12 675")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 2182")
    tran0.writeAction("slorii X16 X16 12 1653")
    tran0.writeAction("movir X17 1946")
    tran0.writeAction("slorii X17 X17 12 2713")
    tran0.writeAction("slorii X17 X17 12 355")
    tran0.writeAction("slorii X17 X17 12 3478")
    tran0.writeAction("slorii X17 X17 12 2681")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
