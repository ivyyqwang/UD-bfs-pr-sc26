from EFA_v2 import *
def fcnvt_64_32_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17682275161028079010]
    tran0.writeAction("movir X16 62820")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("slorii X16 X16 12 769")
    tran0.writeAction("slorii X16 X16 12 3242")
    tran0.writeAction("slorii X16 X16 12 3490")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
