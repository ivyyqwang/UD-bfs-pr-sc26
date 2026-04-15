from EFA_v2 import *
def sraddii_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-895092627870660028, 7, 363]
    tran0.writeAction("movir X16 62355")
    tran0.writeAction("slorii X16 X16 12 4063")
    tran0.writeAction("slorii X16 X16 12 3922")
    tran0.writeAction("slorii X16 X16 12 2860")
    tran0.writeAction("slorii X16 X16 12 2628")
    tran0.writeAction("sraddii X16 X17 7 363")
    tran0.writeAction("yieldt")
    return efa
