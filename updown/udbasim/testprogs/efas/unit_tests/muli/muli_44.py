from EFA_v2 import *
def muli_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3753984640183357043, 28540]
    tran0.writeAction("movir X16 52199")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("slorii X16 X16 12 3061")
    tran0.writeAction("slorii X16 X16 12 2451")
    tran0.writeAction("slorii X16 X16 12 397")
    tran0.writeAction("muli X16 X17 28540")
    tran0.writeAction("yieldt")
    return efa
