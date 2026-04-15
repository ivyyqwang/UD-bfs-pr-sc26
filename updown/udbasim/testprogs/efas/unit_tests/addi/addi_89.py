from EFA_v2 import *
def addi_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-660930012464416982, 18845]
    tran0.writeAction("movir X16 63187")
    tran0.writeAction("slorii X16 X16 12 3706")
    tran0.writeAction("slorii X16 X16 12 1993")
    tran0.writeAction("slorii X16 X16 12 2719")
    tran0.writeAction("slorii X16 X16 12 1834")
    tran0.writeAction("addi X16 X17 18845")
    tran0.writeAction("yieldt")
    return efa
