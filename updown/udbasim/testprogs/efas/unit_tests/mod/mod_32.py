from EFA_v2 import *
def mod_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4905278258722576237, -8419313048367301107]
    tran0.writeAction("movir X16 17427")
    tran0.writeAction("slorii X16 X16 12 201")
    tran0.writeAction("slorii X16 X16 12 1607")
    tran0.writeAction("slorii X16 X16 12 2481")
    tran0.writeAction("slorii X16 X16 12 1901")
    tran0.writeAction("movir X17 35624")
    tran0.writeAction("slorii X17 X17 12 2422")
    tran0.writeAction("slorii X17 X17 12 979")
    tran0.writeAction("slorii X17 X17 12 1047")
    tran0.writeAction("slorii X17 X17 12 3597")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
