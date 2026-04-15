from EFA_v2 import *
def hash_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3478624574284889848, -6408025562243035034]
    tran0.writeAction("movir X16 53177")
    tran0.writeAction("slorii X16 X16 12 1814")
    tran0.writeAction("slorii X16 X16 12 342")
    tran0.writeAction("slorii X16 X16 12 3296")
    tran0.writeAction("slorii X16 X16 12 264")
    tran0.writeAction("movir X17 42770")
    tran0.writeAction("slorii X17 X17 12 491")
    tran0.writeAction("slorii X17 X17 12 970")
    tran0.writeAction("slorii X17 X17 12 3609")
    tran0.writeAction("slorii X17 X17 12 102")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
