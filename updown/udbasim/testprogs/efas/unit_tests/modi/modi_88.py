from EFA_v2 import *
def modi_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5906328968302920026, 28619]
    tran0.writeAction("movir X16 44552")
    tran0.writeAction("slorii X16 X16 12 2065")
    tran0.writeAction("slorii X16 X16 12 2221")
    tran0.writeAction("slorii X16 X16 12 2887")
    tran0.writeAction("slorii X16 X16 12 3750")
    tran0.writeAction("modi X16 X17 28619")
    tran0.writeAction("yieldt")
    return efa
