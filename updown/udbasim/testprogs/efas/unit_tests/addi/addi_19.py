from EFA_v2 import *
def addi_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6669754175077951492, 31131]
    tran0.writeAction("movir X16 41840")
    tran0.writeAction("slorii X16 X16 12 1118")
    tran0.writeAction("slorii X16 X16 12 2663")
    tran0.writeAction("slorii X16 X16 12 1229")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("addi X16 X17 31131")
    tran0.writeAction("yieldt")
    return efa
