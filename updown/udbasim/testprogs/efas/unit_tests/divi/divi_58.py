from EFA_v2 import *
def divi_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4719907461093932558, 20195]
    tran0.writeAction("movir X16 16768")
    tran0.writeAction("slorii X16 X16 12 1965")
    tran0.writeAction("slorii X16 X16 12 1063")
    tran0.writeAction("slorii X16 X16 12 899")
    tran0.writeAction("slorii X16 X16 12 3598")
    tran0.writeAction("divi X16 X17 20195")
    tran0.writeAction("yieldt")
    return efa
