from EFA_v2 import *
def fcnvt_64_b16_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5608373023319522284]
    tran0.writeAction("movir X16 19924")
    tran0.writeAction("slorii X16 X16 12 3864")
    tran0.writeAction("slorii X16 X16 12 3294")
    tran0.writeAction("slorii X16 X16 12 3455")
    tran0.writeAction("slorii X16 X16 12 3052")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
