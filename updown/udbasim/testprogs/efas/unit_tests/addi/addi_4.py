from EFA_v2 import *
def addi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [260289989919199380, 7041]
    tran0.writeAction("movir X16 924")
    tran0.writeAction("slorii X16 X16 12 3013")
    tran0.writeAction("slorii X16 X16 12 3555")
    tran0.writeAction("slorii X16 X16 12 2965")
    tran0.writeAction("slorii X16 X16 12 148")
    tran0.writeAction("addi X16 X17 7041")
    tran0.writeAction("yieldt")
    return efa
