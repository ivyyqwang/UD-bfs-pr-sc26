from EFA_v2 import *
def fadd_64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2420918202134360306, 11771868531165173970]
    tran0.writeAction("movir X16 8600")
    tran0.writeAction("slorii X16 X16 12 3396")
    tran0.writeAction("slorii X16 X16 12 1852")
    tran0.writeAction("slorii X16 X16 12 2031")
    tran0.writeAction("slorii X16 X16 12 242")
    tran0.writeAction("movir X17 41822")
    tran0.writeAction("slorii X17 X17 12 320")
    tran0.writeAction("slorii X17 X17 12 3870")
    tran0.writeAction("slorii X17 X17 12 2865")
    tran0.writeAction("slorii X17 X17 12 2258")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
