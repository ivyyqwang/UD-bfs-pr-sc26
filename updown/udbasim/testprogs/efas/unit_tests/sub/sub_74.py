from EFA_v2 import *
def sub_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9058003017897543517, 1944254794022756345]
    tran0.writeAction("movir X16 33355")
    tran0.writeAction("slorii X16 X16 12 2083")
    tran0.writeAction("slorii X16 X16 12 3871")
    tran0.writeAction("slorii X16 X16 12 3279")
    tran0.writeAction("slorii X16 X16 12 2211")
    tran0.writeAction("movir X17 6907")
    tran0.writeAction("slorii X17 X17 12 1558")
    tran0.writeAction("slorii X17 X17 12 3870")
    tran0.writeAction("slorii X17 X17 12 2361")
    tran0.writeAction("slorii X17 X17 12 4089")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
