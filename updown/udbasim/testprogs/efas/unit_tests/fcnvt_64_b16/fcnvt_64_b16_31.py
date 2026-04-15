from EFA_v2 import *
def fcnvt_64_b16_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16865176890470265729]
    tran0.writeAction("movir X16 59917")
    tran0.writeAction("slorii X16 X16 12 592")
    tran0.writeAction("slorii X16 X16 12 1726")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("slorii X16 X16 12 897")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
