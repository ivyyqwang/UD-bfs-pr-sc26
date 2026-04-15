from EFA_v2 import *
def fcnvt_64_b16_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10068985406682389478]
    tran0.writeAction("movir X16 35772")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 301")
    tran0.writeAction("slorii X16 X16 12 3669")
    tran0.writeAction("slorii X16 X16 12 3046")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
