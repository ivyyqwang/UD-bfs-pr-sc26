from EFA_v2 import *
def divi_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4002899820069598805, 13862]
    tran0.writeAction("movir X16 14221")
    tran0.writeAction("slorii X16 X16 12 642")
    tran0.writeAction("slorii X16 X16 12 3478")
    tran0.writeAction("slorii X16 X16 12 2963")
    tran0.writeAction("slorii X16 X16 12 1621")
    tran0.writeAction("divi X16 X17 13862")
    tran0.writeAction("yieldt")
    return efa
