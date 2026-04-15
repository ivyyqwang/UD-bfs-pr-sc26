from EFA_v2 import *
def fsqrt_32_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1421384932]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 84")
    tran0.writeAction("slorii X16 X16 12 2953")
    tran0.writeAction("slorii X16 X16 12 3300")
    tran0.writeAction("fsqrt.32 X16 X17")
    tran0.writeAction("yieldt")
    return efa
