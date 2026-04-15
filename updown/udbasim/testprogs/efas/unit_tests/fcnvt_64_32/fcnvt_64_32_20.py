from EFA_v2 import *
def fcnvt_64_32_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4366345380751084293]
    tran0.writeAction("movir X16 15512")
    tran0.writeAction("slorii X16 X16 12 1535")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 1376")
    tran0.writeAction("slorii X16 X16 12 2821")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
