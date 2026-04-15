from EFA_v2 import *
def fdiv_64_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12092705955757942875, 12002138910712205671]
    tran0.writeAction("movir X16 42961")
    tran0.writeAction("slorii X16 X16 12 3775")
    tran0.writeAction("slorii X16 X16 12 3890")
    tran0.writeAction("slorii X16 X16 12 830")
    tran0.writeAction("slorii X16 X16 12 2139")
    tran0.writeAction("movir X17 42640")
    tran0.writeAction("slorii X17 X17 12 667")
    tran0.writeAction("slorii X17 X17 12 4045")
    tran0.writeAction("slorii X17 X17 12 3665")
    tran0.writeAction("slorii X17 X17 12 359")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
