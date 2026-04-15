from EFA_v2 import *
def divi_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3166643621035876668, -30380]
    tran0.writeAction("movir X16 11250")
    tran0.writeAction("slorii X16 X16 12 729")
    tran0.writeAction("slorii X16 X16 12 2178")
    tran0.writeAction("slorii X16 X16 12 410")
    tran0.writeAction("slorii X16 X16 12 316")
    tran0.writeAction("divi X16 X17 -30380")
    tran0.writeAction("yieldt")
    return efa
