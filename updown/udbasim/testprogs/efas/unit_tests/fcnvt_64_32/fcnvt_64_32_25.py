from EFA_v2 import *
def fcnvt_64_32_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11914794479923178401]
    tran0.writeAction("movir X16 42329")
    tran0.writeAction("slorii X16 X16 12 3495")
    tran0.writeAction("slorii X16 X16 12 963")
    tran0.writeAction("slorii X16 X16 12 2482")
    tran0.writeAction("slorii X16 X16 12 2977")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
