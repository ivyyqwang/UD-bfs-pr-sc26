from EFA_v2 import *
def modi_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5749152555654176903, 14816]
    tran0.writeAction("movir X16 45110")
    tran0.writeAction("slorii X16 X16 12 3715")
    tran0.writeAction("slorii X16 X16 12 1536")
    tran0.writeAction("slorii X16 X16 12 2881")
    tran0.writeAction("slorii X16 X16 12 3961")
    tran0.writeAction("modi X16 X17 14816")
    tran0.writeAction("yieldt")
    return efa
