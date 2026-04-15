from EFA_v2 import *
def divi_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8237607727900437757, -28541]
    tran0.writeAction("movir X16 29265")
    tran0.writeAction("slorii X16 X16 12 3529")
    tran0.writeAction("slorii X16 X16 12 1396")
    tran0.writeAction("slorii X16 X16 12 2122")
    tran0.writeAction("slorii X16 X16 12 3325")
    tran0.writeAction("divi X16 X17 -28541")
    tran0.writeAction("yieldt")
    return efa
