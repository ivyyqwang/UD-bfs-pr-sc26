from EFA_v2 import *
def addi_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2308811800501538302, -24608]
    tran0.writeAction("movir X16 8202")
    tran0.writeAction("slorii X16 X16 12 2241")
    tran0.writeAction("slorii X16 X16 12 2454")
    tran0.writeAction("slorii X16 X16 12 508")
    tran0.writeAction("slorii X16 X16 12 3582")
    tran0.writeAction("addi X16 X17 -24608")
    tran0.writeAction("yieldt")
    return efa
