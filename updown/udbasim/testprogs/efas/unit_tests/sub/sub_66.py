from EFA_v2 import *
def sub_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7626746405171335518, 2899326146533211911]
    tran0.writeAction("movir X16 27095")
    tran0.writeAction("slorii X16 X16 12 2647")
    tran0.writeAction("slorii X16 X16 12 640")
    tran0.writeAction("slorii X16 X16 12 921")
    tran0.writeAction("slorii X16 X16 12 350")
    tran0.writeAction("movir X17 10300")
    tran0.writeAction("slorii X17 X17 12 1948")
    tran0.writeAction("slorii X17 X17 12 1244")
    tran0.writeAction("slorii X17 X17 12 467")
    tran0.writeAction("slorii X17 X17 12 3847")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
