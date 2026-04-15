from EFA_v2 import *
def modi_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3441350058924878045, -9640]
    tran0.writeAction("movir X16 53309")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 2750")
    tran0.writeAction("slorii X16 X16 12 53")
    tran0.writeAction("slorii X16 X16 12 1827")
    tran0.writeAction("modi X16 X17 -9640")
    tran0.writeAction("yieldt")
    return efa
