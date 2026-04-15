from EFA_v2 import *
def fadd_64_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1611710570873443533, 7409050037818930628]
    tran0.writeAction("movir X16 5725")
    tran0.writeAction("slorii X16 X16 12 3875")
    tran0.writeAction("slorii X16 X16 12 2457")
    tran0.writeAction("slorii X16 X16 12 2677")
    tran0.writeAction("slorii X16 X16 12 1229")
    tran0.writeAction("movir X17 26322")
    tran0.writeAction("slorii X17 X17 12 956")
    tran0.writeAction("slorii X17 X17 12 299")
    tran0.writeAction("slorii X17 X17 12 1195")
    tran0.writeAction("slorii X17 X17 12 1476")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
