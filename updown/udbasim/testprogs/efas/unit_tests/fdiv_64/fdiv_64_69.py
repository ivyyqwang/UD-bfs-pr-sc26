from EFA_v2 import *
def fdiv_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7384664096483930962, 11415968426486202230]
    tran0.writeAction("movir X16 26235")
    tran0.writeAction("slorii X16 X16 12 2445")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 2071")
    tran0.writeAction("slorii X16 X16 12 850")
    tran0.writeAction("movir X17 40557")
    tran0.writeAction("slorii X17 X17 12 2732")
    tran0.writeAction("slorii X17 X17 12 3243")
    tran0.writeAction("slorii X17 X17 12 3215")
    tran0.writeAction("slorii X17 X17 12 3958")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
