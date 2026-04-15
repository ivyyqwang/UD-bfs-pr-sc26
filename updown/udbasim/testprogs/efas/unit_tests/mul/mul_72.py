from EFA_v2 import *
def mul_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3133301763443967003, 9094516289949922139]
    tran0.writeAction("movir X16 54404")
    tran0.writeAction("slorii X16 X16 12 1130")
    tran0.writeAction("slorii X16 X16 12 1447")
    tran0.writeAction("slorii X16 X16 12 3347")
    tran0.writeAction("slorii X16 X16 12 3045")
    tran0.writeAction("movir X17 32310")
    tran0.writeAction("slorii X17 X17 12 870")
    tran0.writeAction("slorii X17 X17 12 386")
    tran0.writeAction("slorii X17 X17 12 1919")
    tran0.writeAction("slorii X17 X17 12 859")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
