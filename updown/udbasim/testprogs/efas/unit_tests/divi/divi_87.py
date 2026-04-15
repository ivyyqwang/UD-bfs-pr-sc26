from EFA_v2 import *
def divi_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5496504106992990973, -1013]
    tran0.writeAction("movir X16 19527")
    tran0.writeAction("slorii X16 X16 12 2069")
    tran0.writeAction("slorii X16 X16 12 3347")
    tran0.writeAction("slorii X16 X16 12 3247")
    tran0.writeAction("slorii X16 X16 12 2813")
    tran0.writeAction("divi X16 X17 -1013")
    tran0.writeAction("yieldt")
    return efa
