from EFA_v2 import *
def divi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9025724379902485922, 16336]
    tran0.writeAction("movir X16 33470")
    tran0.writeAction("slorii X16 X16 12 759")
    tran0.writeAction("slorii X16 X16 12 3887")
    tran0.writeAction("slorii X16 X16 12 1349")
    tran0.writeAction("slorii X16 X16 12 2654")
    tran0.writeAction("divi X16 X17 16336")
    tran0.writeAction("yieldt")
    return efa
