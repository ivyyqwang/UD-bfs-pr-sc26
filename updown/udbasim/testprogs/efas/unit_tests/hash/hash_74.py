from EFA_v2 import *
def hash_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6107183032602153455, -7473106216759340708]
    tran0.writeAction("movir X16 43838")
    tran0.writeAction("slorii X16 X16 12 3798")
    tran0.writeAction("slorii X16 X16 12 923")
    tran0.writeAction("slorii X16 X16 12 1866")
    tran0.writeAction("slorii X16 X16 12 3601")
    tran0.writeAction("movir X17 38986")
    tran0.writeAction("slorii X17 X17 12 791")
    tran0.writeAction("slorii X17 X17 12 3445")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("slorii X17 X17 12 348")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
