from EFA_v2 import *
def subi_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2582135814499499081, 19240]
    tran0.writeAction("movir X16 56362")
    tran0.writeAction("slorii X16 X16 12 1682")
    tran0.writeAction("slorii X16 X16 12 2126")
    tran0.writeAction("slorii X16 X16 12 3864")
    tran0.writeAction("slorii X16 X16 12 951")
    tran0.writeAction("subi X16 X17 19240")
    tran0.writeAction("yieldt")
    return efa
