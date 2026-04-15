from EFA_v2 import *
def fadd_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9791948059564636571, 1860599257668608094]
    tran0.writeAction("movir X16 34787")
    tran0.writeAction("slorii X16 X16 12 4046")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slorii X16 X16 12 1743")
    tran0.writeAction("slorii X16 X16 12 2459")
    tran0.writeAction("movir X17 6610")
    tran0.writeAction("slorii X17 X17 12 722")
    tran0.writeAction("slorii X17 X17 12 2750")
    tran0.writeAction("slorii X17 X17 12 2838")
    tran0.writeAction("slorii X17 X17 12 94")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
