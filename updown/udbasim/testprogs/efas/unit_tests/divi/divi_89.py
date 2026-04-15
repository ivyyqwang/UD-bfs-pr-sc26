from EFA_v2 import *
def divi_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7971939068109201694, 5138]
    tran0.writeAction("movir X16 37213")
    tran0.writeAction("slorii X16 X16 12 4026")
    tran0.writeAction("slorii X16 X16 12 1946")
    tran0.writeAction("slorii X16 X16 12 1197")
    tran0.writeAction("slorii X16 X16 12 3810")
    tran0.writeAction("divi X16 X17 5138")
    tran0.writeAction("yieldt")
    return efa
