from EFA_v2 import *
def sraddii_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-725760264330732127, 14, 1942]
    tran0.writeAction("movir X16 62957")
    tran0.writeAction("slorii X16 X16 12 2382")
    tran0.writeAction("slorii X16 X16 12 644")
    tran0.writeAction("slorii X16 X16 12 1937")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("sraddii X16 X17 14 1942")
    tran0.writeAction("yieldt")
    return efa
