from EFA_v2 import *
def mul_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7600837389215200305, -6334492000214608543]
    tran0.writeAction("movir X16 38532")
    tran0.writeAction("slorii X16 X16 12 1642")
    tran0.writeAction("slorii X16 X16 12 2652")
    tran0.writeAction("slorii X16 X16 12 1312")
    tran0.writeAction("slorii X16 X16 12 3023")
    tran0.writeAction("movir X17 43031")
    tran0.writeAction("slorii X17 X17 12 1489")
    tran0.writeAction("slorii X17 X17 12 1630")
    tran0.writeAction("slorii X17 X17 12 2681")
    tran0.writeAction("slorii X17 X17 12 1377")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
