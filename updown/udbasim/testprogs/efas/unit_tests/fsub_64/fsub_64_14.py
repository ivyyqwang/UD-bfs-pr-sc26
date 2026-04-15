from EFA_v2 import *
def fsub_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1944780819419430835, 4385535874333241591]
    tran0.writeAction("movir X16 6909")
    tran0.writeAction("slorii X16 X16 12 1021")
    tran0.writeAction("slorii X16 X16 12 2547")
    tran0.writeAction("slorii X16 X16 12 1999")
    tran0.writeAction("slorii X16 X16 12 4019")
    tran0.writeAction("movir X17 15580")
    tran0.writeAction("slorii X17 X17 12 2266")
    tran0.writeAction("slorii X17 X17 12 1123")
    tran0.writeAction("slorii X17 X17 12 1495")
    tran0.writeAction("slorii X17 X17 12 247")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
