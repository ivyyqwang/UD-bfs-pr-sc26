from EFA_v2 import *
def mul_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6704011279961189774, 3660089531827053214]
    tran0.writeAction("movir X16 23817")
    tran0.writeAction("slorii X16 X16 12 1771")
    tran0.writeAction("slorii X16 X16 12 3424")
    tran0.writeAction("slorii X16 X16 12 1222")
    tran0.writeAction("slorii X16 X16 12 3470")
    tran0.writeAction("movir X17 13003")
    tran0.writeAction("slorii X17 X17 12 1024")
    tran0.writeAction("slorii X17 X17 12 2438")
    tran0.writeAction("slorii X17 X17 12 2774")
    tran0.writeAction("slorii X17 X17 12 670")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
