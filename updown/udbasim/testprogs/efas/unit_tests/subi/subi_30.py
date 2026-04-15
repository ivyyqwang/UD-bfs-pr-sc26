from EFA_v2 import *
def subi_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1114288574446622331, -30232]
    tran0.writeAction("movir X16 3958")
    tran0.writeAction("slorii X16 X16 12 3064")
    tran0.writeAction("slorii X16 X16 12 3585")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("subi X16 X17 -30232")
    tran0.writeAction("yieldt")
    return efa
