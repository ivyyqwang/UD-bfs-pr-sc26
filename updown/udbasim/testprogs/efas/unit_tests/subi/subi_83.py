from EFA_v2 import *
def subi_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5622794366010371984, -8695]
    tran0.writeAction("movir X16 19976")
    tran0.writeAction("slorii X16 X16 12 730")
    tran0.writeAction("slorii X16 X16 12 3935")
    tran0.writeAction("slorii X16 X16 12 474")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("subi X16 X17 -8695")
    tran0.writeAction("yieldt")
    return efa
