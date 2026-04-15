from EFA_v2 import *
def mod_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4712894998468238783, -49598353729100766]
    tran0.writeAction("movir X16 16743")
    tran0.writeAction("slorii X16 X16 12 2320")
    tran0.writeAction("slorii X16 X16 12 2039")
    tran0.writeAction("slorii X16 X16 12 1697")
    tran0.writeAction("slorii X16 X16 12 3519")
    tran0.writeAction("movir X17 65359")
    tran0.writeAction("slorii X17 X17 12 3240")
    tran0.writeAction("slorii X17 X17 12 3936")
    tran0.writeAction("slorii X17 X17 12 2182")
    tran0.writeAction("slorii X17 X17 12 1058")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
