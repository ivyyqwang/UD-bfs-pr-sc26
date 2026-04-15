from EFA_v2 import *
def fcnvt_64_b16_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13945136878757877148]
    tran0.writeAction("movir X16 49543")
    tran0.writeAction("slorii X16 X16 12 321")
    tran0.writeAction("slorii X16 X16 12 2898")
    tran0.writeAction("slorii X16 X16 12 2305")
    tran0.writeAction("slorii X16 X16 12 1436")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
