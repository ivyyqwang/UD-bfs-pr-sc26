from EFA_v2 import *
def fdiv_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1914937710941002480, 18427334380023663671]
    tran0.writeAction("movir X16 6803")
    tran0.writeAction("slorii X16 X16 12 923")
    tran0.writeAction("slorii X16 X16 12 971")
    tran0.writeAction("slorii X16 X16 12 2613")
    tran0.writeAction("slorii X16 X16 12 2800")
    tran0.writeAction("movir X17 65467")
    tran0.writeAction("slorii X17 X17 12 175")
    tran0.writeAction("slorii X17 X17 12 3206")
    tran0.writeAction("slorii X17 X17 12 2676")
    tran0.writeAction("slorii X17 X17 12 3127")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
