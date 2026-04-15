from EFA_v2 import *
def divi_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6082386959939592664, 12220]
    tran0.writeAction("movir X16 43927")
    tran0.writeAction("slorii X16 X16 12 84")
    tran0.writeAction("slorii X16 X16 12 2346")
    tran0.writeAction("slorii X16 X16 12 1361")
    tran0.writeAction("slorii X16 X16 12 3624")
    tran0.writeAction("divi X16 X17 12220")
    tran0.writeAction("yieldt")
    return efa
