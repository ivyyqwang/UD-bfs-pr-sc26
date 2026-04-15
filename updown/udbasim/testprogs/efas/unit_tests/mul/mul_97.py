from EFA_v2 import *
def mul_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7024723414981255929, -8524769662101102812]
    tran0.writeAction("movir X16 24956")
    tran0.writeAction("slorii X16 X16 12 3403")
    tran0.writeAction("slorii X16 X16 12 2611")
    tran0.writeAction("slorii X16 X16 12 1338")
    tran0.writeAction("slorii X16 X16 12 761")
    tran0.writeAction("movir X17 35249")
    tran0.writeAction("slorii X17 X17 12 3826")
    tran0.writeAction("slorii X17 X17 12 2194")
    tran0.writeAction("slorii X17 X17 12 1789")
    tran0.writeAction("slorii X17 X17 12 3876")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
