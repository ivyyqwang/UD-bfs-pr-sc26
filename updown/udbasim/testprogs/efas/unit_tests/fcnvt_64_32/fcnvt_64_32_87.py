from EFA_v2 import *
def fcnvt_64_32_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11705650583748309939]
    tran0.writeAction("movir X16 41586")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 4045")
    tran0.writeAction("slorii X16 X16 12 663")
    tran0.writeAction("slorii X16 X16 12 947")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
