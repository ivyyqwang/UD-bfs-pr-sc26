from EFA_v2 import *
def fcnvt_i64_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5704273880379694492]
    tran0.writeAction("movir X16 20265")
    tran0.writeAction("slorii X16 X16 12 2669")
    tran0.writeAction("slorii X16 X16 12 3877")
    tran0.writeAction("slorii X16 X16 12 2337")
    tran0.writeAction("slorii X16 X16 12 3484")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
