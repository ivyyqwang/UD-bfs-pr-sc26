from EFA_v2 import *
def fadd_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15691705331374083066, 18268349041686186280]
    tran0.writeAction("movir X16 55748")
    tran0.writeAction("slorii X16 X16 12 557")
    tran0.writeAction("slorii X16 X16 12 3156")
    tran0.writeAction("slorii X16 X16 12 2684")
    tran0.writeAction("slorii X16 X16 12 3066")
    tran0.writeAction("movir X17 64902")
    tran0.writeAction("slorii X17 X17 12 874")
    tran0.writeAction("slorii X17 X17 12 2526")
    tran0.writeAction("slorii X17 X17 12 2264")
    tran0.writeAction("slorii X17 X17 12 2344")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
