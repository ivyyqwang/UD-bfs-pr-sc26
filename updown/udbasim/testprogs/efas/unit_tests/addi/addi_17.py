from EFA_v2 import *
def addi_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5415032273943594978, -18129]
    tran0.writeAction("movir X16 46297")
    tran0.writeAction("slorii X16 X16 12 3853")
    tran0.writeAction("slorii X16 X16 12 1600")
    tran0.writeAction("slorii X16 X16 12 1295")
    tran0.writeAction("slorii X16 X16 12 2078")
    tran0.writeAction("addi X16 X17 -18129")
    tran0.writeAction("yieldt")
    return efa
