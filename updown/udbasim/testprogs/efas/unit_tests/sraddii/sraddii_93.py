from EFA_v2 import *
def sraddii_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7420002520615243652, 7, 649]
    tran0.writeAction("movir X16 26361")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("slorii X16 X16 12 3172")
    tran0.writeAction("slorii X16 X16 12 3972")
    tran0.writeAction("sraddii X16 X17 7 649")
    tran0.writeAction("yieldt")
    return efa
