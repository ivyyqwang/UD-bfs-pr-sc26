from EFA_v2 import *
def muli_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9040946590451422703, -17631]
    tran0.writeAction("movir X16 33416")
    tran0.writeAction("slorii X16 X16 12 431")
    tran0.writeAction("slorii X16 X16 12 2586")
    tran0.writeAction("slorii X16 X16 12 3538")
    tran0.writeAction("slorii X16 X16 12 2577")
    tran0.writeAction("muli X16 X17 -17631")
    tran0.writeAction("yieldt")
    return efa
