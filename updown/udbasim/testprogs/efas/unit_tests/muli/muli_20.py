from EFA_v2 import *
def muli_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5903898609919616518, -12839]
    tran0.writeAction("movir X16 44561")
    tran0.writeAction("slorii X16 X16 12 567")
    tran0.writeAction("slorii X16 X16 12 3733")
    tran0.writeAction("slorii X16 X16 12 3353")
    tran0.writeAction("slorii X16 X16 12 2554")
    tran0.writeAction("muli X16 X17 -12839")
    tran0.writeAction("yieldt")
    return efa
