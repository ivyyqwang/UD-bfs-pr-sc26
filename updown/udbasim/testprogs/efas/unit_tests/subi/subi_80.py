from EFA_v2 import *
def subi_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7914804045303179826, 7917]
    tran0.writeAction("movir X16 28119")
    tran0.writeAction("slorii X16 X16 12 133")
    tran0.writeAction("slorii X16 X16 12 2115")
    tran0.writeAction("slorii X16 X16 12 494")
    tran0.writeAction("slorii X16 X16 12 2610")
    tran0.writeAction("subi X16 X17 7917")
    tran0.writeAction("yieldt")
    return efa
