from EFA_v2 import *
def divi_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1323307457049011503, 7066]
    tran0.writeAction("movir X16 60834")
    tran0.writeAction("slorii X16 X16 12 2734")
    tran0.writeAction("slorii X16 X16 12 261")
    tran0.writeAction("slorii X16 X16 12 3965")
    tran0.writeAction("slorii X16 X16 12 2769")
    tran0.writeAction("divi X16 X17 7066")
    tran0.writeAction("yieldt")
    return efa
