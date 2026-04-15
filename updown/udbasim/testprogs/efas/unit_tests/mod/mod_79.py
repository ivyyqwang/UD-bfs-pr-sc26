from EFA_v2 import *
def mod_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2220906139645966607, 5125943441674202145]
    tran0.writeAction("movir X16 7890")
    tran0.writeAction("slorii X16 X16 12 997")
    tran0.writeAction("slorii X16 X16 12 3581")
    tran0.writeAction("slorii X16 X16 12 335")
    tran0.writeAction("slorii X16 X16 12 2319")
    tran0.writeAction("movir X17 18211")
    tran0.writeAction("slorii X17 X17 12 38")
    tran0.writeAction("slorii X17 X17 12 1755")
    tran0.writeAction("slorii X17 X17 12 3006")
    tran0.writeAction("slorii X17 X17 12 3105")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
