from EFA_v2 import *
def fdiv_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10402473747272042773, 8990289931015103965]
    tran0.writeAction("movir X16 36957")
    tran0.writeAction("slorii X16 X16 12 44")
    tran0.writeAction("slorii X16 X16 12 555")
    tran0.writeAction("slorii X16 X16 12 1952")
    tran0.writeAction("slorii X16 X16 12 2325")
    tran0.writeAction("movir X17 31939")
    tran0.writeAction("slorii X17 X17 12 3792")
    tran0.writeAction("slorii X17 X17 12 3909")
    tran0.writeAction("slorii X17 X17 12 3794")
    tran0.writeAction("slorii X17 X17 12 1501")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
