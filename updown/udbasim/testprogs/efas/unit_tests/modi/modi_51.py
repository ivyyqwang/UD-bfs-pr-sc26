from EFA_v2 import *
def modi_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5806109152588900305, 5772]
    tran0.writeAction("movir X16 44908")
    tran0.writeAction("slorii X16 X16 12 2279")
    tran0.writeAction("slorii X16 X16 12 3296")
    tran0.writeAction("slorii X16 X16 12 3253")
    tran0.writeAction("slorii X16 X16 12 2095")
    tran0.writeAction("modi X16 X17 5772")
    tran0.writeAction("yieldt")
    return efa
