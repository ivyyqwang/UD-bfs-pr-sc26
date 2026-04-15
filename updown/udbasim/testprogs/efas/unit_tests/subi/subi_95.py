from EFA_v2 import *
def subi_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8297446217434488035, -12929]
    tran0.writeAction("movir X16 36057")
    tran0.writeAction("slorii X16 X16 12 2250")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 3722")
    tran0.writeAction("slorii X16 X16 12 797")
    tran0.writeAction("subi X16 X17 -12929")
    tran0.writeAction("yieldt")
    return efa
