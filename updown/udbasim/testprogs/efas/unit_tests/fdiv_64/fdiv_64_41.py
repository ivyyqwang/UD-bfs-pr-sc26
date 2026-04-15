from EFA_v2 import *
def fdiv_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3315284718543361611, 3801265221594731809]
    tran0.writeAction("movir X16 11778")
    tran0.writeAction("slorii X16 X16 12 1054")
    tran0.writeAction("slorii X16 X16 12 746")
    tran0.writeAction("slorii X16 X16 12 237")
    tran0.writeAction("slorii X16 X16 12 1611")
    tran0.writeAction("movir X17 13504")
    tran0.writeAction("slorii X17 X17 12 3305")
    tran0.writeAction("slorii X17 X17 12 1086")
    tran0.writeAction("slorii X17 X17 12 821")
    tran0.writeAction("slorii X17 X17 12 1313")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
