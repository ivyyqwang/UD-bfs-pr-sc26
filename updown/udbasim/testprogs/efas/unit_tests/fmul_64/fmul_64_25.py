from EFA_v2 import *
def fmul_64_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3599967750186600628, 889704045700104915]
    tran0.writeAction("movir X16 12789")
    tran0.writeAction("slorii X16 X16 12 2681")
    tran0.writeAction("slorii X16 X16 12 2152")
    tran0.writeAction("slorii X16 X16 12 3008")
    tran0.writeAction("slorii X16 X16 12 2228")
    tran0.writeAction("movir X17 3160")
    tran0.writeAction("slorii X17 X17 12 3537")
    tran0.writeAction("slorii X17 X17 12 3487")
    tran0.writeAction("slorii X17 X17 12 748")
    tran0.writeAction("slorii X17 X17 12 723")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
