from EFA_v2 import *
def mod_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3468478029740686262, 1144188013177197267]
    tran0.writeAction("movir X16 12322")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("slorii X16 X16 12 1065")
    tran0.writeAction("slorii X16 X16 12 3851")
    tran0.writeAction("slorii X16 X16 12 2998")
    tran0.writeAction("movir X17 4064")
    tran0.writeAction("slorii X17 X17 12 3982")
    tran0.writeAction("slorii X17 X17 12 3985")
    tran0.writeAction("slorii X17 X17 12 2813")
    tran0.writeAction("slorii X17 X17 12 723")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
