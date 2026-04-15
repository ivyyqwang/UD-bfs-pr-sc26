from EFA_v2 import *
def fadd_64_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8038934606245552667, 1497007647383874072]
    tran0.writeAction("movir X16 28560")
    tran0.writeAction("slorii X16 X16 12 134")
    tran0.writeAction("slorii X16 X16 12 3753")
    tran0.writeAction("slorii X16 X16 12 3526")
    tran0.writeAction("slorii X16 X16 12 539")
    tran0.writeAction("movir X17 5318")
    tran0.writeAction("slorii X17 X17 12 1800")
    tran0.writeAction("slorii X17 X17 12 1560")
    tran0.writeAction("slorii X17 X17 12 1470")
    tran0.writeAction("slorii X17 X17 12 2584")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
