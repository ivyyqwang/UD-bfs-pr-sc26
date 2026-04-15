from EFA_v2 import *
def subi_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7768061089754713251, 6319]
    tran0.writeAction("movir X16 37938")
    tran0.writeAction("slorii X16 X16 12 1241")
    tran0.writeAction("slorii X16 X16 12 2183")
    tran0.writeAction("slorii X16 X16 12 2607")
    tran0.writeAction("slorii X16 X16 12 861")
    tran0.writeAction("subi X16 X17 6319")
    tran0.writeAction("yieldt")
    return efa
