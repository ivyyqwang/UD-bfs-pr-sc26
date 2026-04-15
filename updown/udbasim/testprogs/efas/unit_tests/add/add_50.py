from EFA_v2 import *
def add_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-817825251442576715, 8063415444225453792]
    tran0.writeAction("movir X16 62630")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 1103")
    tran0.writeAction("slorii X16 X16 12 1723")
    tran0.writeAction("slorii X16 X16 12 693")
    tran0.writeAction("movir X17 28647")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("slorii X17 X17 12 4077")
    tran0.writeAction("slorii X17 X17 12 1870")
    tran0.writeAction("slorii X17 X17 12 3808")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
