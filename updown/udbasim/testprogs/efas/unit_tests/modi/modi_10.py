from EFA_v2 import *
def modi_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5831110609337181754, -6621]
    tran0.writeAction("movir X16 44819")
    tran0.writeAction("slorii X16 X16 12 3004")
    tran0.writeAction("slorii X16 X16 12 2972")
    tran0.writeAction("slorii X16 X16 12 1825")
    tran0.writeAction("slorii X16 X16 12 2502")
    tran0.writeAction("modi X16 X17 -6621")
    tran0.writeAction("yieldt")
    return efa
