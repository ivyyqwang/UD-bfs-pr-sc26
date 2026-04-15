from EFA_v2 import *
def mul_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3942279692841103227, 33912606292687377]
    tran0.writeAction("movir X16 51530")
    tran0.writeAction("slorii X16 X16 12 856")
    tran0.writeAction("slorii X16 X16 12 422")
    tran0.writeAction("slorii X16 X16 12 3973")
    tran0.writeAction("slorii X16 X16 12 133")
    tran0.writeAction("movir X17 120")
    tran0.writeAction("slorii X17 X17 12 1973")
    tran0.writeAction("slorii X17 X17 12 1523")
    tran0.writeAction("slorii X17 X17 12 1979")
    tran0.writeAction("slorii X17 X17 12 2577")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
