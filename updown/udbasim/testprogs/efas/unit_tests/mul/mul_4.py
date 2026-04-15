from EFA_v2 import *
def mul_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2371326781253833756, 1692387851140813720]
    tran0.writeAction("movir X16 8424")
    tran0.writeAction("slorii X16 X16 12 2642")
    tran0.writeAction("slorii X16 X16 12 1227")
    tran0.writeAction("slorii X16 X16 12 21")
    tran0.writeAction("slorii X16 X16 12 1052")
    tran0.writeAction("movir X17 6012")
    tran0.writeAction("slorii X17 X17 12 2332")
    tran0.writeAction("slorii X17 X17 12 2225")
    tran0.writeAction("slorii X17 X17 12 1781")
    tran0.writeAction("slorii X17 X17 12 920")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
