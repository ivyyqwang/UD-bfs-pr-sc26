from EFA_v2 import *
def addi_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3253085211707981935, -16390]
    tran0.writeAction("movir X16 53978")
    tran0.writeAction("slorii X16 X16 12 2947")
    tran0.writeAction("slorii X16 X16 12 3148")
    tran0.writeAction("slorii X16 X16 12 283")
    tran0.writeAction("slorii X16 X16 12 3985")
    tran0.writeAction("addi X16 X17 -16390")
    tran0.writeAction("yieldt")
    return efa
