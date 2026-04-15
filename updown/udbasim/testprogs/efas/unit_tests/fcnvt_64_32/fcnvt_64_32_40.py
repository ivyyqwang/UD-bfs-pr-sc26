from EFA_v2 import *
def fcnvt_64_32_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5672362067470124570]
    tran0.writeAction("movir X16 20152")
    tran0.writeAction("slorii X16 X16 12 1139")
    tran0.writeAction("slorii X16 X16 12 3892")
    tran0.writeAction("slorii X16 X16 12 3920")
    tran0.writeAction("slorii X16 X16 12 1562")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
