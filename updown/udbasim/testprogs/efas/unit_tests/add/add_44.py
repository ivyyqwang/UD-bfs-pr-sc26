from EFA_v2 import *
def add_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-891829441055904917, 651172476478052140]
    tran0.writeAction("movir X16 62367")
    tran0.writeAction("slorii X16 X16 12 2397")
    tran0.writeAction("slorii X16 X16 12 2357")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("slorii X16 X16 12 2923")
    tran0.writeAction("movir X17 2313")
    tran0.writeAction("slorii X17 X17 12 1758")
    tran0.writeAction("slorii X17 X17 12 2771")
    tran0.writeAction("slorii X17 X17 12 4037")
    tran0.writeAction("slorii X17 X17 12 1836")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
