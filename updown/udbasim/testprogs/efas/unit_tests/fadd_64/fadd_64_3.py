from EFA_v2 import *
def fadd_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7765601621419352306, 12119152001855829897]
    tran0.writeAction("movir X16 27588")
    tran0.writeAction("slorii X16 X16 12 3928")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 3678")
    tran0.writeAction("slorii X16 X16 12 242")
    tran0.writeAction("movir X17 43055")
    tran0.writeAction("slorii X17 X17 12 3592")
    tran0.writeAction("slorii X17 X17 12 2337")
    tran0.writeAction("slorii X17 X17 12 2379")
    tran0.writeAction("slorii X17 X17 12 1929")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
