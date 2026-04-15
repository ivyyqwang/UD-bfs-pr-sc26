from EFA_v2 import *
def sub_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4885659234047872994, -4497416384106170697]
    tran0.writeAction("movir X16 17357")
    tran0.writeAction("slorii X16 X16 12 1427")
    tran0.writeAction("slorii X16 X16 12 35")
    tran0.writeAction("slorii X16 X16 12 124")
    tran0.writeAction("slorii X16 X16 12 4066")
    tran0.writeAction("movir X17 49557")
    tran0.writeAction("slorii X17 X17 12 3962")
    tran0.writeAction("slorii X17 X17 12 130")
    tran0.writeAction("slorii X17 X17 12 1351")
    tran0.writeAction("slorii X17 X17 12 1719")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
