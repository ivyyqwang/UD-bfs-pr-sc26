from EFA_v2 import *
def hash_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2138098724500202392, 1409137753335179798]
    tran0.writeAction("movir X16 7596")
    tran0.writeAction("slorii X16 X16 12 215")
    tran0.writeAction("slorii X16 X16 12 1592")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("movir X17 5006")
    tran0.writeAction("slorii X17 X17 12 1077")
    tran0.writeAction("slorii X17 X17 12 539")
    tran0.writeAction("slorii X17 X17 12 554")
    tran0.writeAction("slorii X17 X17 12 2582")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
