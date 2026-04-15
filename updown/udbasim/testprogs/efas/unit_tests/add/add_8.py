from EFA_v2 import *
def add_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-692325304354412993, 2712581297174143065]
    tran0.writeAction("movir X16 63076")
    tran0.writeAction("slorii X16 X16 12 1500")
    tran0.writeAction("slorii X16 X16 12 3524")
    tran0.writeAction("slorii X16 X16 12 3854")
    tran0.writeAction("slorii X16 X16 12 1599")
    tran0.writeAction("movir X17 9637")
    tran0.writeAction("slorii X17 X17 12 101")
    tran0.writeAction("slorii X17 X17 12 354")
    tran0.writeAction("slorii X17 X17 12 1774")
    tran0.writeAction("slorii X17 X17 12 89")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
