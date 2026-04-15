from EFA_v2 import *
def add_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [343312598764880695, -1751265862592398507]
    tran0.writeAction("movir X16 1219")
    tran0.writeAction("slorii X16 X16 12 2831")
    tran0.writeAction("slorii X16 X16 12 3416")
    tran0.writeAction("slorii X16 X16 12 1216")
    tran0.writeAction("slorii X16 X16 12 823")
    tran0.writeAction("movir X17 59314")
    tran0.writeAction("slorii X17 X17 12 1039")
    tran0.writeAction("slorii X17 X17 12 2560")
    tran0.writeAction("slorii X17 X17 12 3735")
    tran0.writeAction("slorii X17 X17 12 2901")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
