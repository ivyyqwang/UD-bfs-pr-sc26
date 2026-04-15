from EFA_v2 import *
def modi_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6191221662345788920, -22519]
    tran0.writeAction("movir X16 21995")
    tran0.writeAction("slorii X16 X16 12 2612")
    tran0.writeAction("slorii X16 X16 12 3237")
    tran0.writeAction("slorii X16 X16 12 3375")
    tran0.writeAction("slorii X16 X16 12 3576")
    tran0.writeAction("modi X16 X17 -22519")
    tran0.writeAction("yieldt")
    return efa
