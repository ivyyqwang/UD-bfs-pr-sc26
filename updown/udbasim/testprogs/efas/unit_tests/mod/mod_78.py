from EFA_v2 import *
def mod_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8094995453276220530, 975831454584290552]
    tran0.writeAction("movir X16 28759")
    tran0.writeAction("slorii X16 X16 12 823")
    tran0.writeAction("slorii X16 X16 12 2498")
    tran0.writeAction("slorii X16 X16 12 3814")
    tran0.writeAction("slorii X16 X16 12 3186")
    tran0.writeAction("movir X17 3466")
    tran0.writeAction("slorii X17 X17 12 3480")
    tran0.writeAction("slorii X17 X17 12 2475")
    tran0.writeAction("slorii X17 X17 12 611")
    tran0.writeAction("slorii X17 X17 12 3320")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
