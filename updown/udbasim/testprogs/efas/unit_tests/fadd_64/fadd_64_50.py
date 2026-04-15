from EFA_v2 import *
def fadd_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7393198948420132831, 6756556575317524920]
    tran0.writeAction("movir X16 26265")
    tran0.writeAction("slorii X16 X16 12 3764")
    tran0.writeAction("slorii X16 X16 12 1490")
    tran0.writeAction("slorii X16 X16 12 1529")
    tran0.writeAction("slorii X16 X16 12 4063")
    tran0.writeAction("movir X17 24004")
    tran0.writeAction("slorii X17 X17 12 454")
    tran0.writeAction("slorii X17 X17 12 2128")
    tran0.writeAction("slorii X17 X17 12 2584")
    tran0.writeAction("slorii X17 X17 12 440")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
