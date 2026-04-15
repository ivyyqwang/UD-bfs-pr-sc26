from EFA_v2 import *
def fmadd_64_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14196414133983610183, 1653352797820457325, 2925251228220188831]
    tran0.writeAction("movir X16 50435")
    tran0.writeAction("slorii X16 X16 12 3255")
    tran0.writeAction("slorii X16 X16 12 100")
    tran0.writeAction("slorii X16 X16 12 1752")
    tran0.writeAction("slorii X16 X16 12 1351")
    tran0.writeAction("movir X17 5873")
    tran0.writeAction("slorii X17 X17 12 3641")
    tran0.writeAction("slorii X17 X17 12 3098")
    tran0.writeAction("slorii X17 X17 12 1993")
    tran0.writeAction("slorii X17 X17 12 365")
    tran0.writeAction("movir X18 10392")
    tran0.writeAction("slorii X18 X18 12 2375")
    tran0.writeAction("slorii X18 X18 12 3664")
    tran0.writeAction("slorii X18 X18 12 3438")
    tran0.writeAction("slorii X18 X18 12 2207")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
