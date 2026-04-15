from EFA_v2 import *
def modi_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5739501930722416394, 27344]
    tran0.writeAction("movir X16 45145")
    tran0.writeAction("slorii X16 X16 12 790")
    tran0.writeAction("slorii X16 X16 12 1847")
    tran0.writeAction("slorii X16 X16 12 2546")
    tran0.writeAction("slorii X16 X16 12 2294")
    tran0.writeAction("modi X16 X17 27344")
    tran0.writeAction("yieldt")
    return efa
