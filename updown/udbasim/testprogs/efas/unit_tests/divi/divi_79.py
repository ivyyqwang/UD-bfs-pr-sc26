from EFA_v2 import *
def divi_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6774652053503806063, -17050]
    tran0.writeAction("movir X16 24068")
    tran0.writeAction("slorii X16 X16 12 1634")
    tran0.writeAction("slorii X16 X16 12 1573")
    tran0.writeAction("slorii X16 X16 12 3952")
    tran0.writeAction("slorii X16 X16 12 2671")
    tran0.writeAction("divi X16 X17 -17050")
    tran0.writeAction("yieldt")
    return efa
