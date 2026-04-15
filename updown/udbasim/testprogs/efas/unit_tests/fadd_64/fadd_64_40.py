from EFA_v2 import *
def fadd_64_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10112006379684972559, 10586015796225705658]
    tran0.writeAction("movir X16 35925")
    tran0.writeAction("slorii X16 X16 12 259")
    tran0.writeAction("slorii X16 X16 12 2563")
    tran0.writeAction("slorii X16 X16 12 2484")
    tran0.writeAction("slorii X16 X16 12 2063")
    tran0.writeAction("movir X17 37609")
    tran0.writeAction("slorii X17 X17 12 340")
    tran0.writeAction("slorii X17 X17 12 1936")
    tran0.writeAction("slorii X17 X17 12 2896")
    tran0.writeAction("slorii X17 X17 12 1722")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
