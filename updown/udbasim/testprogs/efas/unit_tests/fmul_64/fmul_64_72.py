from EFA_v2 import *
def fmul_64_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13159217782373153600, 2855302444997554795]
    tran0.writeAction("movir X16 46750")
    tran0.writeAction("slorii X16 X16 12 3821")
    tran0.writeAction("slorii X16 X16 12 2624")
    tran0.writeAction("slorii X16 X16 12 1455")
    tran0.writeAction("slorii X16 X16 12 2880")
    tran0.writeAction("movir X17 10144")
    tran0.writeAction("slorii X17 X17 12 295")
    tran0.writeAction("slorii X17 X17 12 536")
    tran0.writeAction("slorii X17 X17 12 1571")
    tran0.writeAction("slorii X17 X17 12 619")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
