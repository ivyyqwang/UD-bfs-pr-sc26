from EFA_v2 import *
def modi_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6178232755511080866, 27035]
    tran0.writeAction("movir X16 21949")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 1307")
    tran0.writeAction("slorii X16 X16 12 3771")
    tran0.writeAction("slorii X16 X16 12 1954")
    tran0.writeAction("modi X16 X17 27035")
    tran0.writeAction("yieldt")
    return efa
