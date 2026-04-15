from EFA_v2 import *
def addi_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5207051258862707163, 30991]
    tran0.writeAction("movir X16 18499")
    tran0.writeAction("slorii X16 X16 12 664")
    tran0.writeAction("slorii X16 X16 12 2083")
    tran0.writeAction("slorii X16 X16 12 3122")
    tran0.writeAction("slorii X16 X16 12 475")
    tran0.writeAction("addi X16 X17 30991")
    tran0.writeAction("yieldt")
    return efa
