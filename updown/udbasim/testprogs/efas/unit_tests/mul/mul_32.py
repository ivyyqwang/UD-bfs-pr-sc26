from EFA_v2 import *
def mul_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4821496949933430202, -9001999053641257827]
    tran0.writeAction("movir X16 17129")
    tran0.writeAction("slorii X16 X16 12 1630")
    tran0.writeAction("slorii X16 X16 12 3642")
    tran0.writeAction("slorii X16 X16 12 1685")
    tran0.writeAction("slorii X16 X16 12 1466")
    tran0.writeAction("movir X17 33554")
    tran0.writeAction("slorii X17 X17 12 1944")
    tran0.writeAction("slorii X17 X17 12 3627")
    tran0.writeAction("slorii X17 X17 12 1270")
    tran0.writeAction("slorii X17 X17 12 3229")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
