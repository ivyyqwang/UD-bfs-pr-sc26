from EFA_v2 import *
def modi_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1999884947484799762, 29569]
    tran0.writeAction("movir X16 7105")
    tran0.writeAction("slorii X16 X16 12 76")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 1975")
    tran0.writeAction("slorii X16 X16 12 786")
    tran0.writeAction("modi X16 X17 29569")
    tran0.writeAction("yieldt")
    return efa
