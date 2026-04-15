from EFA_v2 import *
def div_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8475981967266326431, -7277921866474443900]
    tran0.writeAction("movir X16 30112")
    tran0.writeAction("slorii X16 X16 12 3019")
    tran0.writeAction("slorii X16 X16 12 265")
    tran0.writeAction("slorii X16 X16 12 2154")
    tran0.writeAction("slorii X16 X16 12 1951")
    tran0.writeAction("movir X17 39679")
    tran0.writeAction("slorii X17 X17 12 2569")
    tran0.writeAction("slorii X17 X17 12 3933")
    tran0.writeAction("slorii X17 X17 12 3042")
    tran0.writeAction("slorii X17 X17 12 2948")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
