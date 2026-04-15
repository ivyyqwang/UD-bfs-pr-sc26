from EFA_v2 import *
def mul_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1450258781980218858, -4236984131307400523]
    tran0.writeAction("movir X16 60383")
    tran0.writeAction("slorii X16 X16 12 2645")
    tran0.writeAction("slorii X16 X16 12 595")
    tran0.writeAction("slorii X16 X16 12 2778")
    tran0.writeAction("slorii X16 X16 12 2582")
    tran0.writeAction("movir X17 50483")
    tran0.writeAction("slorii X17 X17 12 854")
    tran0.writeAction("slorii X17 X17 12 398")
    tran0.writeAction("slorii X17 X17 12 1865")
    tran0.writeAction("slorii X17 X17 12 693")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
