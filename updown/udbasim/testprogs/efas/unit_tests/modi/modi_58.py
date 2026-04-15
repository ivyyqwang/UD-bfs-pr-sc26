from EFA_v2 import *
def modi_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4955109296593452699, -21998]
    tran0.writeAction("movir X16 47931")
    tran0.writeAction("slorii X16 X16 12 3749")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 1276")
    tran0.writeAction("slorii X16 X16 12 357")
    tran0.writeAction("modi X16 X17 -21998")
    tran0.writeAction("yieldt")
    return efa
