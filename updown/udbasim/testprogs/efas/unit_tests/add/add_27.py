from EFA_v2 import *
def add_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4302128538529428576, -4482487446701809598]
    tran0.writeAction("movir X16 50251")
    tran0.writeAction("slorii X16 X16 12 3150")
    tran0.writeAction("slorii X16 X16 12 842")
    tran0.writeAction("slorii X16 X16 12 3616")
    tran0.writeAction("slorii X16 X16 12 2976")
    tran0.writeAction("movir X17 49611")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("slorii X17 X17 12 2717")
    tran0.writeAction("slorii X17 X17 12 782")
    tran0.writeAction("slorii X17 X17 12 66")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
