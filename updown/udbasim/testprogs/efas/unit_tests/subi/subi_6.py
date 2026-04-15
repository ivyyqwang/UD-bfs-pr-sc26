from EFA_v2 import *
def subi_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [990126090497416013, 14866]
    tran0.writeAction("movir X16 3517")
    tran0.writeAction("slorii X16 X16 12 2598")
    tran0.writeAction("slorii X16 X16 12 3826")
    tran0.writeAction("slorii X16 X16 12 3869")
    tran0.writeAction("slorii X16 X16 12 2893")
    tran0.writeAction("subi X16 X17 14866")
    tran0.writeAction("yieldt")
    return efa
