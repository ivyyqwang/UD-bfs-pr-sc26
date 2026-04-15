from EFA_v2 import *
def fsqrt_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5417377086673066157]
    tran0.writeAction("movir X16 19246")
    tran0.writeAction("slorii X16 X16 12 1596")
    tran0.writeAction("slorii X16 X16 12 513")
    tran0.writeAction("slorii X16 X16 12 2001")
    tran0.writeAction("slorii X16 X16 12 2221")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
