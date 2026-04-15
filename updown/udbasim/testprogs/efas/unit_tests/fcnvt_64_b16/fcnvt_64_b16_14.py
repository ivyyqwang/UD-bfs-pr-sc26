from EFA_v2 import *
def fcnvt_64_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3131174553248732065]
    tran0.writeAction("movir X16 11124")
    tran0.writeAction("slorii X16 X16 12 682")
    tran0.writeAction("slorii X16 X16 12 2720")
    tran0.writeAction("slorii X16 X16 12 545")
    tran0.writeAction("slorii X16 X16 12 929")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
