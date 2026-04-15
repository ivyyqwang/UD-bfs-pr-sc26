from EFA_v2 import *
def muli_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7485064573507342923, -6862]
    tran0.writeAction("movir X16 26592")
    tran0.writeAction("slorii X16 X16 12 1193")
    tran0.writeAction("slorii X16 X16 12 624")
    tran0.writeAction("slorii X16 X16 12 3137")
    tran0.writeAction("slorii X16 X16 12 587")
    tran0.writeAction("muli X16 X17 -6862")
    tran0.writeAction("yieldt")
    return efa
