from EFA_v2 import *
def modi_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4727309967526498739, 6732]
    tran0.writeAction("movir X16 48741")
    tran0.writeAction("slorii X16 X16 12 906")
    tran0.writeAction("slorii X16 X16 12 386")
    tran0.writeAction("slorii X16 X16 12 1718")
    tran0.writeAction("slorii X16 X16 12 3661")
    tran0.writeAction("modi X16 X17 6732")
    tran0.writeAction("yieldt")
    return efa
