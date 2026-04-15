from EFA_v2 import *
def fdiv_32_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [307918318, 4093556372]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 18")
    tran0.writeAction("slorii X16 X16 12 1447")
    tran0.writeAction("slorii X16 X16 12 1518")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 243")
    tran0.writeAction("slorii X17 X17 12 4075")
    tran0.writeAction("slorii X17 X17 12 1684")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
