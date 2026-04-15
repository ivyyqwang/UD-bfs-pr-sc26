from EFA_v2 import *
def fadd_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6077583935824794634, 17846483984345385453]
    tran0.writeAction("movir X16 21591")
    tran0.writeAction("slorii X16 X16 12 3750")
    tran0.writeAction("slorii X16 X16 12 931")
    tran0.writeAction("slorii X16 X16 12 1873")
    tran0.writeAction("slorii X16 X16 12 1034")
    tran0.writeAction("movir X17 63403")
    tran0.writeAction("slorii X17 X17 12 1834")
    tran0.writeAction("slorii X17 X17 12 264")
    tran0.writeAction("slorii X17 X17 12 2476")
    tran0.writeAction("slorii X17 X17 12 2541")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
