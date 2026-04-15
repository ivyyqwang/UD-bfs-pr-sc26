from EFA_v2 import *
def modi_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6150362672059466202, -29289]
    tran0.writeAction("movir X16 43685")
    tran0.writeAction("slorii X16 X16 12 2139")
    tran0.writeAction("slorii X16 X16 12 3164")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("slorii X16 X16 12 3622")
    tran0.writeAction("modi X16 X17 -29289")
    tran0.writeAction("yieldt")
    return efa
