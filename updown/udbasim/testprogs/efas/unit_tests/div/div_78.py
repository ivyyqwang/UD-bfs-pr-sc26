from EFA_v2 import *
def div_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5656847213464254778, -6973195913276625788]
    tran0.writeAction("movir X16 20097")
    tran0.writeAction("slorii X16 X16 12 649")
    tran0.writeAction("slorii X16 X16 12 451")
    tran0.writeAction("slorii X16 X16 12 799")
    tran0.writeAction("slorii X16 X16 12 2362")
    tran0.writeAction("movir X17 40762")
    tran0.writeAction("slorii X17 X17 12 948")
    tran0.writeAction("slorii X17 X17 12 815")
    tran0.writeAction("slorii X17 X17 12 3854")
    tran0.writeAction("slorii X17 X17 12 3204")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
