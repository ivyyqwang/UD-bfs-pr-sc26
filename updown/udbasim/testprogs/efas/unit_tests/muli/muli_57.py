from EFA_v2 import *
def muli_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3867314013032369088, -5213]
    tran0.writeAction("movir X16 51796")
    tran0.writeAction("slorii X16 X16 12 2214")
    tran0.writeAction("slorii X16 X16 12 1314")
    tran0.writeAction("slorii X16 X16 12 1291")
    tran0.writeAction("slorii X16 X16 12 1088")
    tran0.writeAction("muli X16 X17 -5213")
    tran0.writeAction("yieldt")
    return efa
