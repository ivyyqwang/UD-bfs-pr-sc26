from EFA_v2 import *
def fdiv_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [47176296939879255, 806026718311778365]
    tran0.writeAction("movir X16 167")
    tran0.writeAction("slorii X16 X16 12 2473")
    tran0.writeAction("slorii X16 X16 12 1940")
    tran0.writeAction("slorii X16 X16 12 3767")
    tran0.writeAction("slorii X16 X16 12 2903")
    tran0.writeAction("movir X17 2863")
    tran0.writeAction("slorii X17 X17 12 2384")
    tran0.writeAction("slorii X17 X17 12 1952")
    tran0.writeAction("slorii X17 X17 12 1832")
    tran0.writeAction("slorii X17 X17 12 2109")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
