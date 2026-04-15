from EFA_v2 import *
def fmul_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7902615733487589313, 8782081877749252824]
    tran0.writeAction("movir X16 28075")
    tran0.writeAction("slorii X16 X16 12 2994")
    tran0.writeAction("slorii X16 X16 12 966")
    tran0.writeAction("slorii X16 X16 12 3853")
    tran0.writeAction("slorii X16 X16 12 1985")
    tran0.writeAction("movir X17 31200")
    tran0.writeAction("slorii X17 X17 12 911")
    tran0.writeAction("slorii X17 X17 12 55")
    tran0.writeAction("slorii X17 X17 12 2620")
    tran0.writeAction("slorii X17 X17 12 728")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
