from EFA_v2 import *
def div_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4077027328822649907, -7277484904617442566]
    tran0.writeAction("movir X16 51051")
    tran0.writeAction("slorii X16 X16 12 2003")
    tran0.writeAction("slorii X16 X16 12 3797")
    tran0.writeAction("slorii X16 X16 12 3957")
    tran0.writeAction("slorii X16 X16 12 3021")
    tran0.writeAction("movir X17 39681")
    tran0.writeAction("slorii X17 X17 12 736")
    tran0.writeAction("slorii X17 X17 12 2426")
    tran0.writeAction("slorii X17 X17 12 40")
    tran0.writeAction("slorii X17 X17 12 762")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
