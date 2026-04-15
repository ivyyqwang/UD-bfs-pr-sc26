from EFA_v2 import *
def fsqrt_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18336706116101904687]
    tran0.writeAction("movir X16 65145")
    tran0.writeAction("slorii X16 X16 12 272")
    tran0.writeAction("slorii X16 X16 12 3968")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 2351")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
