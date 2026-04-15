from EFA_v2 import *
def fmul_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11794285849632904798, 10334246078270585882]
    tran0.writeAction("movir X16 41901")
    tran0.writeAction("slorii X16 X16 12 2951")
    tran0.writeAction("slorii X16 X16 12 3534")
    tran0.writeAction("slorii X16 X16 12 3217")
    tran0.writeAction("slorii X16 X16 12 1630")
    tran0.writeAction("movir X17 36714")
    tran0.writeAction("slorii X17 X17 12 2528")
    tran0.writeAction("slorii X17 X17 12 3604")
    tran0.writeAction("slorii X17 X17 12 3243")
    tran0.writeAction("slorii X17 X17 12 3098")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
