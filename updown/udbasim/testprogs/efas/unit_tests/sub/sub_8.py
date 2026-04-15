from EFA_v2 import *
def sub_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6953083065600804710, -8313312511921755668]
    tran0.writeAction("movir X16 40833")
    tran0.writeAction("slorii X16 X16 12 2812")
    tran0.writeAction("slorii X16 X16 12 2677")
    tran0.writeAction("slorii X16 X16 12 327")
    tran0.writeAction("slorii X16 X16 12 2202")
    tran0.writeAction("movir X17 36001")
    tran0.writeAction("slorii X17 X17 12 741")
    tran0.writeAction("slorii X17 X17 12 244")
    tran0.writeAction("slorii X17 X17 12 382")
    tran0.writeAction("slorii X17 X17 12 2540")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
