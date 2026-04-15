from EFA_v2 import *
def fcnvt_64_b16_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1606838140645519508]
    tran0.writeAction("movir X16 5708")
    tran0.writeAction("slorii X16 X16 12 2604")
    tran0.writeAction("slorii X16 X16 12 1672")
    tran0.writeAction("slorii X16 X16 12 2971")
    tran0.writeAction("slorii X16 X16 12 148")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
