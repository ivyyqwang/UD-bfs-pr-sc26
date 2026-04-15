from EFA_v2 import *
def sladdii_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3020461079270831164, 11, 770]
    tran0.writeAction("movir X16 10730")
    tran0.writeAction("slorii X16 X16 12 3413")
    tran0.writeAction("slorii X16 X16 12 2359")
    tran0.writeAction("slorii X16 X16 12 3403")
    tran0.writeAction("slorii X16 X16 12 1084")
    tran0.writeAction("sladdii X16 X17 11 770")
    tran0.writeAction("yieldt")
    return efa
