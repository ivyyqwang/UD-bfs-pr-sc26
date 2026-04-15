from EFA_v2 import *
def subi_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7515379898959066762, 3805]
    tran0.writeAction("movir X16 26699")
    tran0.writeAction("slorii X16 X16 12 4067")
    tran0.writeAction("slorii X16 X16 12 813")
    tran0.writeAction("slorii X16 X16 12 2319")
    tran0.writeAction("slorii X16 X16 12 1674")
    tran0.writeAction("subi X16 X17 3805")
    tran0.writeAction("yieldt")
    return efa
