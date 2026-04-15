from EFA_v2 import *
def fmul_64_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9938202579977993917, 11232914818876204215]
    tran0.writeAction("movir X16 35307")
    tran0.writeAction("slorii X16 X16 12 2409")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("slorii X16 X16 12 1879")
    tran0.writeAction("slorii X16 X16 12 3773")
    tran0.writeAction("movir X17 39907")
    tran0.writeAction("slorii X17 X17 12 1352")
    tran0.writeAction("slorii X17 X17 12 867")
    tran0.writeAction("slorii X17 X17 12 1382")
    tran0.writeAction("slorii X17 X17 12 1207")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
