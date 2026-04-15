from EFA_v2 import *
def fdiv_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [859165366328434255, 11450270497288598331]
    tran0.writeAction("movir X16 3052")
    tran0.writeAction("slorii X16 X16 12 1509")
    tran0.writeAction("slorii X16 X16 12 2367")
    tran0.writeAction("slorii X16 X16 12 1329")
    tran0.writeAction("slorii X16 X16 12 3663")
    tran0.writeAction("movir X17 40679")
    tran0.writeAction("slorii X17 X17 12 2181")
    tran0.writeAction("slorii X17 X17 12 2533")
    tran0.writeAction("slorii X17 X17 12 91")
    tran0.writeAction("slorii X17 X17 12 827")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
