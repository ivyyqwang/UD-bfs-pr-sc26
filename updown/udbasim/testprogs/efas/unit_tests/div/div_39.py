from EFA_v2 import *
def div_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4135152206046014699, -4217970128838023371]
    tran0.writeAction("movir X16 14691")
    tran0.writeAction("slorii X16 X16 12 48")
    tran0.writeAction("slorii X16 X16 12 1469")
    tran0.writeAction("slorii X16 X16 12 2234")
    tran0.writeAction("slorii X16 X16 12 3307")
    tran0.writeAction("movir X17 50550")
    tran0.writeAction("slorii X17 X17 12 3112")
    tran0.writeAction("slorii X17 X17 12 1021")
    tran0.writeAction("slorii X17 X17 12 1642")
    tran0.writeAction("slorii X17 X17 12 1845")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
