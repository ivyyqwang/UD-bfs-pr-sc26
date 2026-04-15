from EFA_v2 import *
def sub_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1273546171924244503, -8226049520347179285]
    tran0.writeAction("movir X16 61011")
    tran0.writeAction("slorii X16 X16 12 1864")
    tran0.writeAction("slorii X16 X16 12 273")
    tran0.writeAction("slorii X16 X16 12 1625")
    tran0.writeAction("slorii X16 X16 12 2025")
    tran0.writeAction("movir X17 36311")
    tran0.writeAction("slorii X17 X17 12 824")
    tran0.writeAction("slorii X17 X17 12 2930")
    tran0.writeAction("slorii X17 X17 12 3825")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
