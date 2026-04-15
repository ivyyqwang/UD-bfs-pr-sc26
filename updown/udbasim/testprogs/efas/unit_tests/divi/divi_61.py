from EFA_v2 import *
def divi_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5056669297416734810, -31702]
    tran0.writeAction("movir X16 17964")
    tran0.writeAction("slorii X16 X16 12 3678")
    tran0.writeAction("slorii X16 X16 12 3907")
    tran0.writeAction("slorii X16 X16 12 608")
    tran0.writeAction("slorii X16 X16 12 2138")
    tran0.writeAction("divi X16 X17 -31702")
    tran0.writeAction("yieldt")
    return efa
