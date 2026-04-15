from EFA_v2 import *
def fadd_64_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4726721561536329166, 9311825991791304881]
    tran0.writeAction("movir X16 16792")
    tran0.writeAction("slorii X16 X16 12 2819")
    tran0.writeAction("slorii X16 X16 12 1931")
    tran0.writeAction("slorii X16 X16 12 2263")
    tran0.writeAction("slorii X16 X16 12 1486")
    tran0.writeAction("movir X17 33082")
    tran0.writeAction("slorii X17 X17 12 1030")
    tran0.writeAction("slorii X17 X17 12 1858")
    tran0.writeAction("slorii X17 X17 12 3974")
    tran0.writeAction("slorii X17 X17 12 177")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
