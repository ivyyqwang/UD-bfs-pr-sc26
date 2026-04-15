from EFA_v2 import *
def subi_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4495548779714785961, 4662]
    tran0.writeAction("movir X16 49564")
    tran0.writeAction("slorii X16 X16 12 2467")
    tran0.writeAction("slorii X16 X16 12 1034")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("slorii X16 X16 12 3415")
    tran0.writeAction("subi X16 X17 4662")
    tran0.writeAction("yieldt")
    return efa
