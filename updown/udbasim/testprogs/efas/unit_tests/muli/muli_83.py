from EFA_v2 import *
def muli_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1273361639532862454, -1606]
    tran0.writeAction("movir X16 4523")
    tran0.writeAction("slorii X16 X16 12 3642")
    tran0.writeAction("slorii X16 X16 12 2594")
    tran0.writeAction("slorii X16 X16 12 3953")
    tran0.writeAction("slorii X16 X16 12 3062")
    tran0.writeAction("muli X16 X17 -1606")
    tran0.writeAction("yieldt")
    return efa
