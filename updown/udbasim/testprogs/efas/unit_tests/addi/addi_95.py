from EFA_v2 import *
def addi_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1893962840086346364, -7518]
    tran0.writeAction("movir X16 58807")
    tran0.writeAction("slorii X16 X16 12 1197")
    tran0.writeAction("slorii X16 X16 12 1250")
    tran0.writeAction("slorii X16 X16 12 3536")
    tran0.writeAction("slorii X16 X16 12 1412")
    tran0.writeAction("addi X16 X17 -7518")
    tran0.writeAction("yieldt")
    return efa
