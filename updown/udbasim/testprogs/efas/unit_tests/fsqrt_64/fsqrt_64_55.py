from EFA_v2 import *
def fsqrt_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2208542497070545746]
    tran0.writeAction("movir X16 7846")
    tran0.writeAction("slorii X16 X16 12 1307")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("slorii X16 X16 12 999")
    tran0.writeAction("slorii X16 X16 12 2898")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
