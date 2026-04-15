from EFA_v2 import *
def fadd_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5798982257894076325, 6695611135090399668]
    tran0.writeAction("movir X16 20602")
    tran0.writeAction("slorii X16 X16 12 506")
    tran0.writeAction("slorii X16 X16 12 932")
    tran0.writeAction("slorii X16 X16 12 2330")
    tran0.writeAction("slorii X16 X16 12 4005")
    tran0.writeAction("movir X17 23787")
    tran0.writeAction("slorii X17 X17 12 2413")
    tran0.writeAction("slorii X17 X17 12 2621")
    tran0.writeAction("slorii X17 X17 12 873")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
