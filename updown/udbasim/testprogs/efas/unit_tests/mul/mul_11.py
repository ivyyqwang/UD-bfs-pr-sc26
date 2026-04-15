from EFA_v2 import *
def mul_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-273665949937694034, 7798223709084435645]
    tran0.writeAction("movir X16 64563")
    tran0.writeAction("slorii X16 X16 12 3044")
    tran0.writeAction("slorii X16 X16 12 1210")
    tran0.writeAction("slorii X16 X16 12 3456")
    tran0.writeAction("slorii X16 X16 12 2734")
    tran0.writeAction("movir X17 27704")
    tran0.writeAction("slorii X17 X17 12 3506")
    tran0.writeAction("slorii X17 X17 12 1419")
    tran0.writeAction("slorii X17 X17 12 28")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
