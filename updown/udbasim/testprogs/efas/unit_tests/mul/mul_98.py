from EFA_v2 import *
def mul_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4776108146921260661, -1583676386094203655]
    tran0.writeAction("movir X16 48567")
    tran0.writeAction("slorii X16 X16 12 3503")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("slorii X16 X16 12 3723")
    tran0.writeAction("slorii X16 X16 12 2443")
    tran0.writeAction("movir X17 59909")
    tran0.writeAction("slorii X17 X17 12 2667")
    tran0.writeAction("slorii X17 X17 12 1967")
    tran0.writeAction("slorii X17 X17 12 2787")
    tran0.writeAction("slorii X17 X17 12 3321")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
