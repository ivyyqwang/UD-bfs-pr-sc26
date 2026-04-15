from EFA_v2 import *
def sub_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7176342326365107835, -3613458890889376750]
    tran0.writeAction("movir X16 25495")
    tran0.writeAction("slorii X16 X16 12 2005")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("slorii X16 X16 12 2427")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("movir X17 52698")
    tran0.writeAction("slorii X17 X17 12 1700")
    tran0.writeAction("slorii X17 X17 12 2206")
    tran0.writeAction("slorii X17 X17 12 252")
    tran0.writeAction("slorii X17 X17 12 3090")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
