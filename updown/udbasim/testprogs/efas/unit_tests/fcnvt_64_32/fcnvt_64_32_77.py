from EFA_v2 import *
def fcnvt_64_32_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6948446562723447618]
    tran0.writeAction("movir X16 24685")
    tran0.writeAction("slorii X16 X16 12 3445")
    tran0.writeAction("slorii X16 X16 12 1431")
    tran0.writeAction("slorii X16 X16 12 3748")
    tran0.writeAction("slorii X16 X16 12 834")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
