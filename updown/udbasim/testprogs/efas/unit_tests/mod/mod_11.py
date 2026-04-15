from EFA_v2 import *
def mod_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-866935980755907132, -3316390188855890189]
    tran0.writeAction("movir X16 62456")
    tran0.writeAction("slorii X16 X16 12 101")
    tran0.writeAction("slorii X16 X16 12 408")
    tran0.writeAction("slorii X16 X16 12 160")
    tran0.writeAction("slorii X16 X16 12 3524")
    tran0.writeAction("movir X17 53753")
    tran0.writeAction("slorii X17 X17 12 3339")
    tran0.writeAction("slorii X17 X17 12 440")
    tran0.writeAction("slorii X17 X17 12 2678")
    tran0.writeAction("slorii X17 X17 12 3827")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
