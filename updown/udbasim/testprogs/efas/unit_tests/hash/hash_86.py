from EFA_v2 import *
def hash_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3786246829245329677, 510583689628335473]
    tran0.writeAction("movir X16 13451")
    tran0.writeAction("slorii X16 X16 12 1846")
    tran0.writeAction("slorii X16 X16 12 3657")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 269")
    tran0.writeAction("movir X17 1813")
    tran0.writeAction("slorii X17 X17 12 3922")
    tran0.writeAction("slorii X17 X17 12 2328")
    tran0.writeAction("slorii X17 X17 12 1659")
    tran0.writeAction("slorii X17 X17 12 3441")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
