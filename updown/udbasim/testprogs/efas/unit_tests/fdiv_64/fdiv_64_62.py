from EFA_v2 import *
def fdiv_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9859698064716888408, 1066433636604900380]
    tran0.writeAction("movir X16 35028")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("slorii X16 X16 12 1700")
    tran0.writeAction("slorii X16 X16 12 231")
    tran0.writeAction("slorii X16 X16 12 2392")
    tran0.writeAction("movir X17 3788")
    tran0.writeAction("slorii X17 X17 12 3003")
    tran0.writeAction("slorii X17 X17 12 3590")
    tran0.writeAction("slorii X17 X17 12 1487")
    tran0.writeAction("slorii X17 X17 12 1052")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
