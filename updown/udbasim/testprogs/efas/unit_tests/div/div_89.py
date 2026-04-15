from EFA_v2 import *
def div_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [749666255789537717, 7800072071605125208]
    tran0.writeAction("movir X16 2663")
    tran0.writeAction("slorii X16 X16 12 1431")
    tran0.writeAction("slorii X16 X16 12 3292")
    tran0.writeAction("slorii X16 X16 12 1771")
    tran0.writeAction("slorii X16 X16 12 2485")
    tran0.writeAction("movir X17 27711")
    tran0.writeAction("slorii X17 X17 12 1731")
    tran0.writeAction("slorii X17 X17 12 2298")
    tran0.writeAction("slorii X17 X17 12 1920")
    tran0.writeAction("slorii X17 X17 12 88")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
