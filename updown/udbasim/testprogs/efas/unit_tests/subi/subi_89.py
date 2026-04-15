from EFA_v2 import *
def subi_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7236627782186037408, -24877]
    tran0.writeAction("movir X16 25709")
    tran0.writeAction("slorii X16 X16 12 2730")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("slorii X16 X16 12 3775")
    tran0.writeAction("slorii X16 X16 12 160")
    tran0.writeAction("subi X16 X17 -24877")
    tran0.writeAction("yieldt")
    return efa
