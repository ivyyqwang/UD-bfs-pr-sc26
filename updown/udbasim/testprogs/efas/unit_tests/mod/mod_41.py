from EFA_v2 import *
def mod_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5176666284100874199, -6139681608494964915]
    tran0.writeAction("movir X16 18391")
    tran0.writeAction("slorii X16 X16 12 872")
    tran0.writeAction("slorii X16 X16 12 3816")
    tran0.writeAction("slorii X16 X16 12 2350")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("movir X17 43723")
    tran0.writeAction("slorii X17 X17 12 1921")
    tran0.writeAction("slorii X17 X17 12 2883")
    tran0.writeAction("slorii X17 X17 12 2697")
    tran0.writeAction("slorii X17 X17 12 3917")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
