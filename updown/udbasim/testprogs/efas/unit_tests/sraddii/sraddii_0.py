from EFA_v2 import *
def sraddii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6305283721313501065, 3, 353]
    tran0.writeAction("movir X16 22400")
    tran0.writeAction("slorii X16 X16 12 3554")
    tran0.writeAction("slorii X16 X16 12 832")
    tran0.writeAction("slorii X16 X16 12 3867")
    tran0.writeAction("slorii X16 X16 12 3977")
    tran0.writeAction("sraddii X16 X17 3 353")
    tran0.writeAction("yieldt")
    return efa
