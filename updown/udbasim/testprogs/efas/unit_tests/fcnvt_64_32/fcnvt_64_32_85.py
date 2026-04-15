from EFA_v2 import *
def fcnvt_64_32_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8639420383335081362]
    tran0.writeAction("movir X16 30693")
    tran0.writeAction("slorii X16 X16 12 1585")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("slorii X16 X16 12 3918")
    tran0.writeAction("slorii X16 X16 12 1426")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
