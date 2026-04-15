from EFA_v2 import *
def hash_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8543357696013591027, -8159245458130158036]
    tran0.writeAction("movir X16 35183")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("slorii X16 X16 12 172")
    tran0.writeAction("slorii X16 X16 12 41")
    tran0.writeAction("slorii X16 X16 12 3597")
    tran0.writeAction("movir X17 36548")
    tran0.writeAction("slorii X17 X17 12 2199")
    tran0.writeAction("slorii X17 X17 12 3136")
    tran0.writeAction("slorii X17 X17 12 3819")
    tran0.writeAction("slorii X17 X17 12 3628")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
