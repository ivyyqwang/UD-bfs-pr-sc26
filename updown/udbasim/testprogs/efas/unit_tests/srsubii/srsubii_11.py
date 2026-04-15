from EFA_v2 import *
def srsubii_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2152043893441647043, 9, 106]
    tran0.writeAction("movir X16 57890")
    tran0.writeAction("slorii X16 X16 12 1655")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("slorii X16 X16 12 1482")
    tran0.writeAction("slorii X16 X16 12 3645")
    tran0.writeAction("srsubii X16 X17 9 106")
    tran0.writeAction("yieldt")
    return efa
