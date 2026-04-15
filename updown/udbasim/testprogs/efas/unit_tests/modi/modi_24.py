from EFA_v2 import *
def modi_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6330621585056858569, 19569]
    tran0.writeAction("movir X16 43045")
    tran0.writeAction("slorii X16 X16 12 467")
    tran0.writeAction("slorii X16 X16 12 1439")
    tran0.writeAction("slorii X16 X16 12 1087")
    tran0.writeAction("slorii X16 X16 12 3639")
    tran0.writeAction("modi X16 X17 19569")
    tran0.writeAction("yieldt")
    return efa
