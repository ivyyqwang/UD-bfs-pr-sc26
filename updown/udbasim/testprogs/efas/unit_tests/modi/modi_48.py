from EFA_v2 import *
def modi_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3874894950490623261, -13188]
    tran0.writeAction("movir X16 51769")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slorii X16 X16 12 662")
    tran0.writeAction("slorii X16 X16 12 211")
    tran0.writeAction("slorii X16 X16 12 739")
    tran0.writeAction("modi X16 X17 -13188")
    tran0.writeAction("yieldt")
    return efa
