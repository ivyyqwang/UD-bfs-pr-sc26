from EFA_v2 import *
def fadd_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11661494164698113771, 974625434487783704]
    tran0.writeAction("movir X16 41429")
    tran0.writeAction("slorii X16 X16 12 3890")
    tran0.writeAction("slorii X16 X16 12 2133")
    tran0.writeAction("slorii X16 X16 12 498")
    tran0.writeAction("slorii X16 X16 12 1771")
    tran0.writeAction("movir X17 3462")
    tran0.writeAction("slorii X17 X17 12 2314")
    tran0.writeAction("slorii X17 X17 12 2875")
    tran0.writeAction("slorii X17 X17 12 2888")
    tran0.writeAction("slorii X17 X17 12 280")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
