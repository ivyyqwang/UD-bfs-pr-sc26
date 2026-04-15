from EFA_v2 import *
def modi_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3335611818012202278, -21746]
    tran0.writeAction("movir X16 53685")
    tran0.writeAction("slorii X16 X16 12 2155")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("slorii X16 X16 12 3226")
    tran0.writeAction("slorii X16 X16 12 2778")
    tran0.writeAction("modi X16 X17 -21746")
    tran0.writeAction("yieldt")
    return efa
