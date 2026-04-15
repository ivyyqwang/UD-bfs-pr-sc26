from EFA_v2 import *
def divi_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5769127111727292578, -13671]
    tran0.writeAction("movir X16 45039")
    tran0.writeAction("slorii X16 X16 12 3863")
    tran0.writeAction("slorii X16 X16 12 1345")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("slorii X16 X16 12 3934")
    tran0.writeAction("divi X16 X17 -13671")
    tran0.writeAction("yieldt")
    return efa
