from EFA_v2 import *
def mod_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4377810166549543040, 4924601148760811940]
    tran0.writeAction("movir X16 49982")
    tran0.writeAction("slorii X16 X16 12 3661")
    tran0.writeAction("slorii X16 X16 12 2336")
    tran0.writeAction("slorii X16 X16 12 2952")
    tran0.writeAction("slorii X16 X16 12 1920")
    tran0.writeAction("movir X17 17495")
    tran0.writeAction("slorii X17 X17 12 2858")
    tran0.writeAction("slorii X17 X17 12 1844")
    tran0.writeAction("slorii X17 X17 12 1510")
    tran0.writeAction("slorii X17 X17 12 2468")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
