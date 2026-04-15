from EFA_v2 import *
def fdiv_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9306891404010873648, 5073521058964796166]
    tran0.writeAction("movir X16 33064")
    tran0.writeAction("slorii X16 X16 12 2950")
    tran0.writeAction("slorii X16 X16 12 3075")
    tran0.writeAction("slorii X16 X16 12 838")
    tran0.writeAction("slorii X16 X16 12 816")
    tran0.writeAction("movir X17 18024")
    tran0.writeAction("slorii X17 X17 12 3144")
    tran0.writeAction("slorii X17 X17 12 1472")
    tran0.writeAction("slorii X17 X17 12 247")
    tran0.writeAction("slorii X17 X17 12 774")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
