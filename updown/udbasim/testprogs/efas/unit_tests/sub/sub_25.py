from EFA_v2 import *
def sub_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9189397899351744250, 4616858988772762949]
    tran0.writeAction("movir X16 32888")
    tran0.writeAction("slorii X16 X16 12 2868")
    tran0.writeAction("slorii X16 X16 12 3149")
    tran0.writeAction("slorii X16 X16 12 1714")
    tran0.writeAction("slorii X16 X16 12 262")
    tran0.writeAction("movir X17 16402")
    tran0.writeAction("slorii X17 X17 12 1548")
    tran0.writeAction("slorii X17 X17 12 2563")
    tran0.writeAction("slorii X17 X17 12 3562")
    tran0.writeAction("slorii X17 X17 12 1349")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
