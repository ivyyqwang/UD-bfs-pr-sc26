from EFA_v2 import *
def muli_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8740262334852902334, -10448]
    tran0.writeAction("movir X16 34484")
    tran0.writeAction("slorii X16 X16 12 1435")
    tran0.writeAction("slorii X16 X16 12 1759")
    tran0.writeAction("slorii X16 X16 12 1501")
    tran0.writeAction("slorii X16 X16 12 578")
    tran0.writeAction("muli X16 X17 -10448")
    tran0.writeAction("yieldt")
    return efa
