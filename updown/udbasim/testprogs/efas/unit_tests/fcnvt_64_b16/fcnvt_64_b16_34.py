from EFA_v2 import *
def fcnvt_64_b16_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13283413464739451415]
    tran0.writeAction("movir X16 47192")
    tran0.writeAction("slorii X16 X16 12 674")
    tran0.writeAction("slorii X16 X16 12 2794")
    tran0.writeAction("slorii X16 X16 12 1785")
    tran0.writeAction("slorii X16 X16 12 535")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
