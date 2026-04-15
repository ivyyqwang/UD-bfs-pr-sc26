from EFA_v2 import *
def hash_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3123561581360432612, 1877610783672954745]
    tran0.writeAction("movir X16 11097")
    tran0.writeAction("slorii X16 X16 12 491")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 188")
    tran0.writeAction("slorii X16 X16 12 1508")
    tran0.writeAction("movir X17 6670")
    tran0.writeAction("slorii X17 X17 12 2512")
    tran0.writeAction("slorii X17 X17 12 3915")
    tran0.writeAction("slorii X17 X17 12 1102")
    tran0.writeAction("slorii X17 X17 12 3961")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
