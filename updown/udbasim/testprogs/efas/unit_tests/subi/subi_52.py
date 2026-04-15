from EFA_v2 import *
def subi_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6199005872514462684, -6336]
    tran0.writeAction("movir X16 22023")
    tran0.writeAction("slorii X16 X16 12 1199")
    tran0.writeAction("slorii X16 X16 12 3919")
    tran0.writeAction("slorii X16 X16 12 3215")
    tran0.writeAction("slorii X16 X16 12 988")
    tran0.writeAction("subi X16 X17 -6336")
    tran0.writeAction("yieldt")
    return efa
