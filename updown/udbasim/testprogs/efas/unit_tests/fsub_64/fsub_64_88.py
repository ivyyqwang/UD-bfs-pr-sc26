from EFA_v2 import *
def fsub_64_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2261788010241491449, 4327937345789052871]
    tran0.writeAction("movir X16 8035")
    tran0.writeAction("slorii X16 X16 12 1987")
    tran0.writeAction("slorii X16 X16 12 1595")
    tran0.writeAction("slorii X16 X16 12 2792")
    tran0.writeAction("slorii X16 X16 12 505")
    tran0.writeAction("movir X17 15375")
    tran0.writeAction("slorii X17 X17 12 3777")
    tran0.writeAction("slorii X17 X17 12 1513")
    tran0.writeAction("slorii X17 X17 12 3700")
    tran0.writeAction("slorii X17 X17 12 1991")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
