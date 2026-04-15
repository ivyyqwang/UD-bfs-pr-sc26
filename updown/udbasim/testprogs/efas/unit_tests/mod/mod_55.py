from EFA_v2 import *
def mod_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8916408040030561147, -7475707609844115155]
    tran0.writeAction("movir X16 33858")
    tran0.writeAction("slorii X16 X16 12 2274")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("slorii X16 X16 12 2217")
    tran0.writeAction("slorii X16 X16 12 3205")
    tran0.writeAction("movir X17 38976")
    tran0.writeAction("slorii X17 X17 12 3896")
    tran0.writeAction("slorii X17 X17 12 2414")
    tran0.writeAction("slorii X17 X17 12 2281")
    tran0.writeAction("slorii X17 X17 12 2349")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
