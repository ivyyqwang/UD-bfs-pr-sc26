from EFA_v2 import *
def muli_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5293087753274981074, -16448]
    tran0.writeAction("movir X16 46731")
    tran0.writeAction("slorii X16 X16 12 715")
    tran0.writeAction("slorii X16 X16 12 2941")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 1326")
    tran0.writeAction("muli X16 X17 -16448")
    tran0.writeAction("yieldt")
    return efa
