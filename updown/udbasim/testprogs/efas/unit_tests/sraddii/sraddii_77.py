from EFA_v2 import *
def sraddii_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2654938857906223543, 5, 410]
    tran0.writeAction("movir X16 9432")
    tran0.writeAction("slorii X16 X16 12 973")
    tran0.writeAction("slorii X16 X16 12 805")
    tran0.writeAction("slorii X16 X16 12 3611")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("sraddii X16 X17 5 410")
    tran0.writeAction("yieldt")
    return efa
