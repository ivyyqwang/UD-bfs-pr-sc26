from EFA_v2 import *
def fdiv_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18361958967347409562, 9361721475829621523]
    tran0.writeAction("movir X16 65234")
    tran0.writeAction("slorii X16 X16 12 3206")
    tran0.writeAction("slorii X16 X16 12 1309")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("slorii X16 X16 12 666")
    tran0.writeAction("movir X17 33259")
    tran0.writeAction("slorii X17 X17 12 2113")
    tran0.writeAction("slorii X17 X17 12 1260")
    tran0.writeAction("slorii X17 X17 12 3974")
    tran0.writeAction("slorii X17 X17 12 787")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
