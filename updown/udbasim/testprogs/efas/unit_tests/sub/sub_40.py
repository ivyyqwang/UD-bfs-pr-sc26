from EFA_v2 import *
def sub_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1800554222696245149, -4287565863043202104]
    tran0.writeAction("movir X16 59139")
    tran0.writeAction("slorii X16 X16 12 599")
    tran0.writeAction("slorii X16 X16 12 2405")
    tran0.writeAction("slorii X16 X16 12 1477")
    tran0.writeAction("slorii X16 X16 12 2147")
    tran0.writeAction("movir X17 50303")
    tran0.writeAction("slorii X17 X17 12 2073")
    tran0.writeAction("slorii X17 X17 12 102")
    tran0.writeAction("slorii X17 X17 12 896")
    tran0.writeAction("slorii X17 X17 12 968")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
