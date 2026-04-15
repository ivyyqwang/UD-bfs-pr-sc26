from EFA_v2 import *
def subi_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5970461341575902037, 24756]
    tran0.writeAction("movir X16 44324")
    tran0.writeAction("slorii X16 X16 12 2704")
    tran0.writeAction("slorii X16 X16 12 2798")
    tran0.writeAction("slorii X16 X16 12 680")
    tran0.writeAction("slorii X16 X16 12 3243")
    tran0.writeAction("subi X16 X17 24756")
    tran0.writeAction("yieldt")
    return efa
