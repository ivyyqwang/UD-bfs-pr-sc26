from EFA_v2 import *
def fsub_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11203211190183829819, 9358368377970022797]
    tran0.writeAction("movir X16 39801")
    tran0.writeAction("slorii X16 X16 12 3283")
    tran0.writeAction("slorii X16 X16 12 2150")
    tran0.writeAction("slorii X16 X16 12 2410")
    tran0.writeAction("slorii X16 X16 12 315")
    tran0.writeAction("movir X17 33247")
    tran0.writeAction("slorii X17 X17 12 2471")
    tran0.writeAction("slorii X17 X17 12 1278")
    tran0.writeAction("slorii X17 X17 12 621")
    tran0.writeAction("slorii X17 X17 12 2445")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
