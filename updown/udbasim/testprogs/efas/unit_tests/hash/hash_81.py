from EFA_v2 import *
def hash_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4476479038454631196, 4910022357165670309]
    tran0.writeAction("movir X16 15903")
    tran0.writeAction("slorii X16 X16 12 2655")
    tran0.writeAction("slorii X16 X16 12 2003")
    tran0.writeAction("slorii X16 X16 12 2336")
    tran0.writeAction("slorii X16 X16 12 2844")
    tran0.writeAction("movir X17 17443")
    tran0.writeAction("slorii X17 X17 12 3701")
    tran0.writeAction("slorii X17 X17 12 454")
    tran0.writeAction("slorii X17 X17 12 351")
    tran0.writeAction("slorii X17 X17 12 4005")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
