from EFA_v2 import *
def modi_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6073805107659424360, -29681]
    tran0.writeAction("movir X16 43957")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("slorii X16 X16 12 3931")
    tran0.writeAction("slorii X16 X16 12 27")
    tran0.writeAction("slorii X16 X16 12 3480")
    tran0.writeAction("modi X16 X17 -29681")
    tran0.writeAction("yieldt")
    return efa
