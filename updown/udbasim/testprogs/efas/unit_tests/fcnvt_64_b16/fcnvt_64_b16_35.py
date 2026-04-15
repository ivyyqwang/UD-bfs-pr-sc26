from EFA_v2 import *
def fcnvt_64_b16_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6190152985975604897]
    tran0.writeAction("movir X16 21991")
    tran0.writeAction("slorii X16 X16 12 3445")
    tran0.writeAction("slorii X16 X16 12 2058")
    tran0.writeAction("slorii X16 X16 12 1636")
    tran0.writeAction("slorii X16 X16 12 1697")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
