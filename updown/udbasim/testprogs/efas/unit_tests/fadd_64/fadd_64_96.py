from EFA_v2 import *
def fadd_64_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8581547684062045725, 16345661376754501048]
    tran0.writeAction("movir X16 30487")
    tran0.writeAction("slorii X16 X16 12 3202")
    tran0.writeAction("slorii X16 X16 12 1747")
    tran0.writeAction("slorii X16 X16 12 2434")
    tran0.writeAction("slorii X16 X16 12 1565")
    tran0.writeAction("movir X17 58071")
    tran0.writeAction("slorii X17 X17 12 1862")
    tran0.writeAction("slorii X17 X17 12 2892")
    tran0.writeAction("slorii X17 X17 12 1124")
    tran0.writeAction("slorii X17 X17 12 1464")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
