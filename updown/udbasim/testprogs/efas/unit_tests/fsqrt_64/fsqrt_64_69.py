from EFA_v2 import *
def fsqrt_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7010064145051360150]
    tran0.writeAction("movir X16 24904")
    tran0.writeAction("slorii X16 X16 12 3075")
    tran0.writeAction("slorii X16 X16 12 754")
    tran0.writeAction("slorii X16 X16 12 2001")
    tran0.writeAction("slorii X16 X16 12 2966")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
