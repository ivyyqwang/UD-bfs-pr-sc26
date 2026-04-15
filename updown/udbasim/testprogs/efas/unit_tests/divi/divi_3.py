from EFA_v2 import *
def divi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7237458386083381499, -29633]
    tran0.writeAction("movir X16 25712")
    tran0.writeAction("slorii X16 X16 12 2528")
    tran0.writeAction("slorii X16 X16 12 3699")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("divi X16 X17 -29633")
    tran0.writeAction("yieldt")
    return efa
