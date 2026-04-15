from EFA_v2 import *
def sub_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8454414048483731460, 8522903936643170507]
    tran0.writeAction("movir X16 35499")
    tran0.writeAction("slorii X16 X16 12 3635")
    tran0.writeAction("slorii X16 X16 12 1888")
    tran0.writeAction("slorii X16 X16 12 225")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("movir X17 30279")
    tran0.writeAction("slorii X17 X17 12 1791")
    tran0.writeAction("slorii X17 X17 12 2398")
    tran0.writeAction("slorii X17 X17 12 1616")
    tran0.writeAction("slorii X17 X17 12 203")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
