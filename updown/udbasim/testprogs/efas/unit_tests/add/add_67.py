from EFA_v2 import *
def add_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1255570401873677078, -4999953897691213921]
    tran0.writeAction("movir X16 4460")
    tran0.writeAction("slorii X16 X16 12 2794")
    tran0.writeAction("slorii X16 X16 12 210")
    tran0.writeAction("slorii X16 X16 12 716")
    tran0.writeAction("slorii X16 X16 12 2838")
    tran0.writeAction("movir X17 47772")
    tran0.writeAction("slorii X17 X17 12 2438")
    tran0.writeAction("slorii X17 X17 12 3010")
    tran0.writeAction("slorii X17 X17 12 3216")
    tran0.writeAction("slorii X17 X17 12 3999")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
