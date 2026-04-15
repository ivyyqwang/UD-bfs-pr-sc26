from EFA_v2 import *
def mul_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4955387941711186101, -7746674873377096869]
    tran0.writeAction("movir X16 17605")
    tran0.writeAction("slorii X16 X16 12 305")
    tran0.writeAction("slorii X16 X16 12 1029")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 2229")
    tran0.writeAction("movir X17 38014")
    tran0.writeAction("slorii X17 X17 12 1155")
    tran0.writeAction("slorii X17 X17 12 3853")
    tran0.writeAction("slorii X17 X17 12 3743")
    tran0.writeAction("slorii X17 X17 12 2907")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
