from EFA_v2 import *
def muli_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2003638863363509211, -17412]
    tran0.writeAction("movir X16 58417")
    tran0.writeAction("slorii X16 X16 12 2641")
    tran0.writeAction("slorii X16 X16 12 459")
    tran0.writeAction("slorii X16 X16 12 207")
    tran0.writeAction("slorii X16 X16 12 1061")
    tran0.writeAction("muli X16 X17 -17412")
    tran0.writeAction("yieldt")
    return efa
