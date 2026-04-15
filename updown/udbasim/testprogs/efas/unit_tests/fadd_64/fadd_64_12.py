from EFA_v2 import *
def fadd_64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11954573146666707642, 18060308492129735228]
    tran0.writeAction("movir X16 42471")
    tran0.writeAction("slorii X16 X16 12 719")
    tran0.writeAction("slorii X16 X16 12 88")
    tran0.writeAction("slorii X16 X16 12 2018")
    tran0.writeAction("slorii X16 X16 12 2746")
    tran0.writeAction("movir X17 64163")
    tran0.writeAction("slorii X17 X17 12 430")
    tran0.writeAction("slorii X17 X17 12 719")
    tran0.writeAction("slorii X17 X17 12 1489")
    tran0.writeAction("slorii X17 X17 12 572")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
