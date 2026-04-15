from EFA_v2 import *
def addi_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8984943441570701477, 9422]
    tran0.writeAction("movir X16 33615")
    tran0.writeAction("slorii X16 X16 12 280")
    tran0.writeAction("slorii X16 X16 12 2894")
    tran0.writeAction("slorii X16 X16 12 829")
    tran0.writeAction("slorii X16 X16 12 3931")
    tran0.writeAction("addi X16 X17 9422")
    tran0.writeAction("yieldt")
    return efa
