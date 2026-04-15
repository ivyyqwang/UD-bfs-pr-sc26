from EFA_v2 import *
def div_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-78940620108266260, -3601322649895852120]
    tran0.writeAction("movir X16 65255")
    tran0.writeAction("slorii X16 X16 12 2238")
    tran0.writeAction("slorii X16 X16 12 3228")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("slorii X16 X16 12 1260")
    tran0.writeAction("movir X17 52741")
    tran0.writeAction("slorii X17 X17 12 2178")
    tran0.writeAction("slorii X17 X17 12 363")
    tran0.writeAction("slorii X17 X17 12 1594")
    tran0.writeAction("slorii X17 X17 12 1960")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
