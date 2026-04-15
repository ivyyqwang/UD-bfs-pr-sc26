from EFA_v2 import *
def hash_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2667192552361391881, 3739976296824613040]
    tran0.writeAction("movir X16 56060")
    tran0.writeAction("slorii X16 X16 12 936")
    tran0.writeAction("slorii X16 X16 12 328")
    tran0.writeAction("slorii X16 X16 12 3816")
    tran0.writeAction("slorii X16 X16 12 2295")
    tran0.writeAction("movir X17 13287")
    tran0.writeAction("slorii X17 X17 12 266")
    tran0.writeAction("slorii X17 X17 12 112")
    tran0.writeAction("slorii X17 X17 12 2506")
    tran0.writeAction("slorii X17 X17 12 2224")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
