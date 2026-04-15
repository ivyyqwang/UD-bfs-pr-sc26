from EFA_v2 import *
def divi_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7570509673049211250, -11958]
    tran0.writeAction("movir X16 26895")
    tran0.writeAction("slorii X16 X16 12 3494")
    tran0.writeAction("slorii X16 X16 12 4086")
    tran0.writeAction("slorii X16 X16 12 3100")
    tran0.writeAction("slorii X16 X16 12 370")
    tran0.writeAction("divi X16 X17 -11958")
    tran0.writeAction("yieldt")
    return efa
