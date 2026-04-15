from EFA_v2 import *
def fdiv_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14952347350513294910, 18379286664348048482]
    tran0.writeAction("movir X16 53121")
    tran0.writeAction("slorii X16 X16 12 1675")
    tran0.writeAction("slorii X16 X16 12 449")
    tran0.writeAction("slorii X16 X16 12 2449")
    tran0.writeAction("slorii X16 X16 12 3646")
    tran0.writeAction("movir X17 65296")
    tran0.writeAction("slorii X17 X17 12 1405")
    tran0.writeAction("slorii X17 X17 12 2037")
    tran0.writeAction("slorii X17 X17 12 2209")
    tran0.writeAction("slorii X17 X17 12 3170")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
