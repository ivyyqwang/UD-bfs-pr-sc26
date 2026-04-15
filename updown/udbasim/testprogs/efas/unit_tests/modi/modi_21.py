from EFA_v2 import *
def modi_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6455832775858249501, -12953]
    tran0.writeAction("movir X16 42600")
    tran0.writeAction("slorii X16 X16 12 1124")
    tran0.writeAction("slorii X16 X16 12 2937")
    tran0.writeAction("slorii X16 X16 12 2642")
    tran0.writeAction("slorii X16 X16 12 227")
    tran0.writeAction("modi X16 X17 -12953")
    tran0.writeAction("yieldt")
    return efa
