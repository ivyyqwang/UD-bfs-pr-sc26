from EFA_v2 import *
def mul_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8350262107905160853, 6686315621585401746]
    tran0.writeAction("movir X16 29666")
    tran0.writeAction("slorii X16 X16 12 370")
    tran0.writeAction("slorii X16 X16 12 1347")
    tran0.writeAction("slorii X16 X16 12 375")
    tran0.writeAction("slorii X16 X16 12 1685")
    tran0.writeAction("movir X17 23754")
    tran0.writeAction("slorii X17 X17 12 2314")
    tran0.writeAction("slorii X17 X17 12 472")
    tran0.writeAction("slorii X17 X17 12 3043")
    tran0.writeAction("slorii X17 X17 12 1938")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
