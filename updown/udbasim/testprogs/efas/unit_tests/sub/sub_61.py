from EFA_v2 import *
def sub_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5255587903000143664, -4431047362089497027]
    tran0.writeAction("movir X16 46864")
    tran0.writeAction("slorii X16 X16 12 1642")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("slorii X16 X16 12 3425")
    tran0.writeAction("slorii X16 X16 12 2256")
    tran0.writeAction("movir X17 49793")
    tran0.writeAction("slorii X17 X17 12 3102")
    tran0.writeAction("slorii X17 X17 12 1695")
    tran0.writeAction("slorii X17 X17 12 2964")
    tran0.writeAction("slorii X17 X17 12 3645")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
