from EFA_v2 import *
def muli_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8033981474081258317, 1760]
    tran0.writeAction("movir X16 36993")
    tran0.writeAction("slorii X16 X16 12 2310")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("slorii X16 X16 12 1300")
    tran0.writeAction("slorii X16 X16 12 1203")
    tran0.writeAction("muli X16 X17 1760")
    tran0.writeAction("yieldt")
    return efa
