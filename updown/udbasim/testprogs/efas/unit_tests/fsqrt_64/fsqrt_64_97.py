from EFA_v2 import *
def fsqrt_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18288878142052350949]
    tran0.writeAction("movir X16 64975")
    tran0.writeAction("slorii X16 X16 12 604")
    tran0.writeAction("slorii X16 X16 12 1413")
    tran0.writeAction("slorii X16 X16 12 1787")
    tran0.writeAction("slorii X16 X16 12 3045")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
