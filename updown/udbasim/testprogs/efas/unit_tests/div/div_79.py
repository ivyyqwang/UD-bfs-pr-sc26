from EFA_v2 import *
def div_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8804196365912079248, -2590965475959805975]
    tran0.writeAction("movir X16 34257")
    tran0.writeAction("slorii X16 X16 12 864")
    tran0.writeAction("slorii X16 X16 12 3397")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("slorii X16 X16 12 1136")
    tran0.writeAction("movir X17 56331")
    tran0.writeAction("slorii X17 X17 12 170")
    tran0.writeAction("slorii X17 X17 12 140")
    tran0.writeAction("slorii X17 X17 12 470")
    tran0.writeAction("slorii X17 X17 12 2025")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
