from EFA_v2 import *
def fdiv_64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3098734858726414674, 1878053703471007205]
    tran0.writeAction("movir X16 11008")
    tran0.writeAction("slorii X16 X16 12 3758")
    tran0.writeAction("slorii X16 X16 12 4011")
    tran0.writeAction("slorii X16 X16 12 2081")
    tran0.writeAction("slorii X16 X16 12 2386")
    tran0.writeAction("movir X17 6672")
    tran0.writeAction("slorii X17 X17 12 766")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 12 2032")
    tran0.writeAction("slorii X17 X17 12 1509")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
