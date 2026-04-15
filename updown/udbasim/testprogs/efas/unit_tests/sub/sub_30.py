from EFA_v2 import *
def sub_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2249200668052882600, 6500050238790064203]
    tran0.writeAction("movir X16 7990")
    tran0.writeAction("slorii X16 X16 12 3137")
    tran0.writeAction("slorii X16 X16 12 1855")
    tran0.writeAction("slorii X16 X16 12 3536")
    tran0.writeAction("slorii X16 X16 12 1192")
    tran0.writeAction("movir X17 23092")
    tran0.writeAction("slorii X17 X17 12 3348")
    tran0.writeAction("slorii X17 X17 12 225")
    tran0.writeAction("slorii X17 X17 12 1125")
    tran0.writeAction("slorii X17 X17 12 2123")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
