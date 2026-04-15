from EFA_v2 import *
def muli_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1256295710321322022, 21521]
    tran0.writeAction("movir X16 61072")
    tran0.writeAction("slorii X16 X16 12 3035")
    tran0.writeAction("slorii X16 X16 12 1317")
    tran0.writeAction("slorii X16 X16 12 1845")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("muli X16 X17 21521")
    tran0.writeAction("yieldt")
    return efa
