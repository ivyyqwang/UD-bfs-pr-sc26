from EFA_v2 import *
def fmul_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2763692795990890631, 8773582116044409469]
    tran0.writeAction("movir X16 9818")
    tran0.writeAction("slorii X16 X16 12 2495")
    tran0.writeAction("slorii X16 X16 12 1165")
    tran0.writeAction("slorii X16 X16 12 1405")
    tran0.writeAction("slorii X16 X16 12 2183")
    tran0.writeAction("movir X17 31170")
    tran0.writeAction("slorii X17 X17 12 103")
    tran0.writeAction("slorii X17 X17 12 826")
    tran0.writeAction("slorii X17 X17 12 2240")
    tran0.writeAction("slorii X17 X17 12 2685")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
