from EFA_v2 import *
def mul_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2984797683803470141, 7310139321352717192]
    tran0.writeAction("movir X16 54931")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 538")
    tran0.writeAction("slorii X16 X16 12 1988")
    tran0.writeAction("slorii X16 X16 12 1731")
    tran0.writeAction("movir X17 25970")
    tran0.writeAction("slorii X17 X17 12 3407")
    tran0.writeAction("slorii X17 X17 12 2915")
    tran0.writeAction("slorii X17 X17 12 3456")
    tran0.writeAction("slorii X17 X17 12 904")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
