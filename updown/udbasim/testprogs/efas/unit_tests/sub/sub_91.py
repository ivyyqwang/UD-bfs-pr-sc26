from EFA_v2 import *
def sub_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2661826476417239441, -3387906441413535333]
    tran0.writeAction("movir X16 56079")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slorii X16 X16 12 3123")
    tran0.writeAction("slorii X16 X16 12 1723")
    tran0.writeAction("slorii X16 X16 12 1647")
    tran0.writeAction("movir X17 53499")
    tran0.writeAction("slorii X17 X17 12 3024")
    tran0.writeAction("slorii X17 X17 12 2715")
    tran0.writeAction("slorii X17 X17 12 1181")
    tran0.writeAction("slorii X17 X17 12 2459")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
