from EFA_v2 import *
def muli_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6684398620148718211, -10738]
    tran0.writeAction("movir X16 41788")
    tran0.writeAction("slorii X16 X16 12 1005")
    tran0.writeAction("slorii X16 X16 12 3796")
    tran0.writeAction("slorii X16 X16 12 3786")
    tran0.writeAction("slorii X16 X16 12 1405")
    tran0.writeAction("muli X16 X17 -10738")
    tran0.writeAction("yieldt")
    return efa
