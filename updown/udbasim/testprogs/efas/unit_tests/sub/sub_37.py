from EFA_v2 import *
def sub_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5202446854902568011, -6389825973525886913]
    tran0.writeAction("movir X16 47053")
    tran0.writeAction("slorii X16 X16 12 802")
    tran0.writeAction("slorii X16 X16 12 1586")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("slorii X16 X16 12 2997")
    tran0.writeAction("movir X17 42834")
    tran0.writeAction("slorii X17 X17 12 3186")
    tran0.writeAction("slorii X17 X17 12 447")
    tran0.writeAction("slorii X17 X17 12 1740")
    tran0.writeAction("slorii X17 X17 12 2111")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
