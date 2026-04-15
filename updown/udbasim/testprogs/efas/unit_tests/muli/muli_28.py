from EFA_v2 import *
def muli_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4829213647167618419, -31454]
    tran0.writeAction("movir X16 17156")
    tran0.writeAction("slorii X16 X16 12 3331")
    tran0.writeAction("slorii X16 X16 12 2511")
    tran0.writeAction("slorii X16 X16 12 3663")
    tran0.writeAction("slorii X16 X16 12 3443")
    tran0.writeAction("muli X16 X17 -31454")
    tran0.writeAction("yieldt")
    return efa
