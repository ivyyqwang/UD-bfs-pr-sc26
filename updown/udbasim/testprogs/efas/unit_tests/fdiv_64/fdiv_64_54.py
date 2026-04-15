from EFA_v2 import *
def fdiv_64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6440828421381780234, 5582165191976387981]
    tran0.writeAction("movir X16 22882")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("slorii X16 X16 12 771")
    tran0.writeAction("slorii X16 X16 12 2871")
    tran0.writeAction("slorii X16 X16 12 778")
    tran0.writeAction("movir X17 19831")
    tran0.writeAction("slorii X17 X17 12 3418")
    tran0.writeAction("slorii X17 X17 12 2721")
    tran0.writeAction("slorii X17 X17 12 1240")
    tran0.writeAction("slorii X17 X17 12 1421")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
