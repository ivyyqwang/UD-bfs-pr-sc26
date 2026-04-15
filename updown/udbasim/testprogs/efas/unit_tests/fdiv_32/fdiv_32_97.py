from EFA_v2 import *
def fdiv_32_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [339471362, 1713498982]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 20")
    tran0.writeAction("slorii X16 X16 12 958")
    tran0.writeAction("slorii X16 X16 12 3074")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 102")
    tran0.writeAction("slorii X17 X17 12 542")
    tran0.writeAction("slorii X17 X17 12 2918")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
