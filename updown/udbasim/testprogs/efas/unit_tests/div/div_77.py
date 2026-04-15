from EFA_v2 import *
def div_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3781513938628567255, 3685734507745709833]
    tran0.writeAction("movir X16 52101")
    tran0.writeAction("slorii X16 X16 12 1489")
    tran0.writeAction("slorii X16 X16 12 2990")
    tran0.writeAction("slorii X16 X16 12 3505")
    tran0.writeAction("slorii X16 X16 12 3881")
    tran0.writeAction("movir X17 13094")
    tran0.writeAction("slorii X17 X17 12 1472")
    tran0.writeAction("slorii X17 X17 12 454")
    tran0.writeAction("slorii X17 X17 12 2384")
    tran0.writeAction("slorii X17 X17 12 3849")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
