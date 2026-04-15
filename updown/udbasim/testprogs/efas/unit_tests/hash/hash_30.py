from EFA_v2 import *
def hash_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7752614735895206691, -7085500465647441963]
    tran0.writeAction("movir X16 37993")
    tran0.writeAction("slorii X16 X16 12 735")
    tran0.writeAction("slorii X16 X16 12 2314")
    tran0.writeAction("slorii X16 X16 12 2078")
    tran0.writeAction("slorii X16 X16 12 1245")
    tran0.writeAction("movir X17 40363")
    tran0.writeAction("slorii X17 X17 12 1005")
    tran0.writeAction("slorii X17 X17 12 3577")
    tran0.writeAction("slorii X17 X17 12 898")
    tran0.writeAction("slorii X17 X17 12 2005")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
