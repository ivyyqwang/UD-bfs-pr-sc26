from EFA_v2 import *
def div_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2570808500036529877, 8981746766770253428]
    tran0.writeAction("movir X16 56402")
    tran0.writeAction("slorii X16 X16 12 2676")
    tran0.writeAction("slorii X16 X16 12 2617")
    tran0.writeAction("slorii X16 X16 12 3145")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("movir X17 31909")
    tran0.writeAction("slorii X17 X17 12 2353")
    tran0.writeAction("slorii X17 X17 12 2263")
    tran0.writeAction("slorii X17 X17 12 3498")
    tran0.writeAction("slorii X17 X17 12 3700")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
