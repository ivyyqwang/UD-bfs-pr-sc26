from EFA_v2 import *
def fadd_64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7853765563466385839, 17421494744073792085]
    tran0.writeAction("movir X16 27902")
    tran0.writeAction("slorii X16 X16 12 738")
    tran0.writeAction("slorii X16 X16 12 2879")
    tran0.writeAction("slorii X16 X16 12 2496")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("movir X17 61893")
    tran0.writeAction("slorii X17 X17 12 2386")
    tran0.writeAction("slorii X17 X17 12 2732")
    tran0.writeAction("slorii X17 X17 12 3494")
    tran0.writeAction("slorii X17 X17 12 2645")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
