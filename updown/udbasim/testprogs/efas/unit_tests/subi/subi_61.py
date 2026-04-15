from EFA_v2 import *
def subi_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3542470161218394864, 21978]
    tran0.writeAction("movir X16 52950")
    tran0.writeAction("slorii X16 X16 12 2530")
    tran0.writeAction("slorii X16 X16 12 2109")
    tran0.writeAction("slorii X16 X16 12 642")
    tran0.writeAction("slorii X16 X16 12 1296")
    tran0.writeAction("subi X16 X17 21978")
    tran0.writeAction("yieldt")
    return efa
