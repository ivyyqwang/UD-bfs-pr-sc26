from EFA_v2 import *
def muli_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1517433455029309441, -11376]
    tran0.writeAction("movir X16 60144")
    tran0.writeAction("slorii X16 X16 12 4068")
    tran0.writeAction("slorii X16 X16 12 4086")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("muli X16 X17 -11376")
    tran0.writeAction("yieldt")
    return efa
