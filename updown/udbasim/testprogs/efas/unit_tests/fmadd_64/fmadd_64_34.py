from EFA_v2 import *
def fmadd_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7214814285123132912, 10966121570592562362, 12042807197251617439]
    tran0.writeAction("movir X16 25632")
    tran0.writeAction("slorii X16 X16 12 693")
    tran0.writeAction("slorii X16 X16 12 3545")
    tran0.writeAction("slorii X16 X16 12 729")
    tran0.writeAction("slorii X16 X16 12 3568")
    tran0.writeAction("movir X17 38959")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("slorii X17 X17 12 1962")
    tran0.writeAction("slorii X17 X17 12 3761")
    tran0.writeAction("slorii X17 X17 12 3258")
    tran0.writeAction("movir X18 42784")
    tran0.writeAction("slorii X18 X18 12 2645")
    tran0.writeAction("slorii X18 X18 12 1826")
    tran0.writeAction("slorii X18 X18 12 2868")
    tran0.writeAction("slorii X18 X18 12 671")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
