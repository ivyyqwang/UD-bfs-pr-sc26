from EFA_v2 import *
def fcnvt_64_b16_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5181713078924115750]
    tran0.writeAction("movir X16 18409")
    tran0.writeAction("slorii X16 X16 12 585")
    tran0.writeAction("slorii X16 X16 12 1893")
    tran0.writeAction("slorii X16 X16 12 1095")
    tran0.writeAction("slorii X16 X16 12 3878")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
