from EFA_v2 import *
def divi_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8572728833360618563, -17816]
    tran0.writeAction("movir X16 30456")
    tran0.writeAction("slorii X16 X16 12 1847")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 854")
    tran0.writeAction("slorii X16 X16 12 1091")
    tran0.writeAction("divi X16 X17 -17816")
    tran0.writeAction("yieldt")
    return efa
