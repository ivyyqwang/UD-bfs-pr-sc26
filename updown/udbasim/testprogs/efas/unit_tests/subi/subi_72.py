from EFA_v2 import *
def subi_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1204591946461683874, -25437]
    tran0.writeAction("movir X16 61256")
    tran0.writeAction("slorii X16 X16 12 1760")
    tran0.writeAction("slorii X16 X16 12 451")
    tran0.writeAction("slorii X16 X16 12 3501")
    tran0.writeAction("slorii X16 X16 12 3934")
    tran0.writeAction("subi X16 X17 -25437")
    tran0.writeAction("yieldt")
    return efa
