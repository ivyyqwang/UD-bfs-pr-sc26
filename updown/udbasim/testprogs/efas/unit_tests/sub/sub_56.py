from EFA_v2 import *
def sub_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1492844192678358807, -3791806729153055175]
    tran0.writeAction("movir X16 5303")
    tran0.writeAction("slorii X16 X16 12 2654")
    tran0.writeAction("slorii X16 X16 12 577")
    tran0.writeAction("slorii X16 X16 12 2450")
    tran0.writeAction("slorii X16 X16 12 3863")
    tran0.writeAction("movir X17 52064")
    tran0.writeAction("slorii X17 X17 12 3261")
    tran0.writeAction("slorii X17 X17 12 3747")
    tran0.writeAction("slorii X17 X17 12 3671")
    tran0.writeAction("slorii X17 X17 12 1593")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
