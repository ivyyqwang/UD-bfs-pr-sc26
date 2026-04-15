from EFA_v2 import *
def div_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7182541776041019690, -4023502083751807565]
    tran0.writeAction("movir X16 25517")
    tran0.writeAction("slorii X16 X16 12 2107")
    tran0.writeAction("slorii X16 X16 12 201")
    tran0.writeAction("slorii X16 X16 12 1344")
    tran0.writeAction("slorii X16 X16 12 2346")
    tran0.writeAction("movir X17 51241")
    tran0.writeAction("slorii X17 X17 12 2658")
    tran0.writeAction("slorii X17 X17 12 3096")
    tran0.writeAction("slorii X17 X17 12 3807")
    tran0.writeAction("slorii X17 X17 12 1459")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
