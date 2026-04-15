from EFA_v2 import *
def subi_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1647105395924725668, 24041]
    tran0.writeAction("movir X16 5851")
    tran0.writeAction("slorii X16 X16 12 2842")
    tran0.writeAction("slorii X16 X16 12 383")
    tran0.writeAction("slorii X16 X16 12 2958")
    tran0.writeAction("slorii X16 X16 12 4004")
    tran0.writeAction("subi X16 X17 24041")
    tran0.writeAction("yieldt")
    return efa
