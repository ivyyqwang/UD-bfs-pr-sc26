from EFA_v2 import *
def mul_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5340161528317618745, 2194993256385349008]
    tran0.writeAction("movir X16 46563")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("slorii X16 X16 12 549")
    tran0.writeAction("slorii X16 X16 12 1725")
    tran0.writeAction("slorii X16 X16 12 1479")
    tran0.writeAction("movir X17 7798")
    tran0.writeAction("slorii X17 X17 12 747")
    tran0.writeAction("slorii X17 X17 12 3251")
    tran0.writeAction("slorii X17 X17 12 928")
    tran0.writeAction("slorii X17 X17 12 1424")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
