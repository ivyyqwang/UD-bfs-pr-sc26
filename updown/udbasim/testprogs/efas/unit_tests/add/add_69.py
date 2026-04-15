from EFA_v2 import *
def add_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1289034655108415108, 8597898866339351117]
    tran0.writeAction("movir X16 4579")
    tran0.writeAction("slorii X16 X16 12 2339")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 3707")
    tran0.writeAction("slorii X16 X16 12 3716")
    tran0.writeAction("movir X17 30545")
    tran0.writeAction("slorii X17 X17 12 3575")
    tran0.writeAction("slorii X17 X17 12 1822")
    tran0.writeAction("slorii X17 X17 12 3648")
    tran0.writeAction("slorii X17 X17 12 2637")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
