from EFA_v2 import *
def hash_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4818402493832331038, -692436911015872420]
    tran0.writeAction("movir X16 17118")
    tran0.writeAction("slorii X16 X16 12 1656")
    tran0.writeAction("slorii X16 X16 12 2565")
    tran0.writeAction("slorii X16 X16 12 2999")
    tran0.writeAction("slorii X16 X16 12 3870")
    tran0.writeAction("movir X17 63075")
    tran0.writeAction("slorii X17 X17 12 3972")
    tran0.writeAction("slorii X17 X17 12 3153")
    tran0.writeAction("slorii X17 X17 12 2171")
    tran0.writeAction("slorii X17 X17 12 2140")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
