from EFA_v2 import *
def addi_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4321131962567871523, 16447]
    tran0.writeAction("movir X16 50184")
    tran0.writeAction("slorii X16 X16 12 1045")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("slorii X16 X16 12 2275")
    tran0.writeAction("slorii X16 X16 12 989")
    tran0.writeAction("addi X16 X17 16447")
    tran0.writeAction("yieldt")
    return efa
