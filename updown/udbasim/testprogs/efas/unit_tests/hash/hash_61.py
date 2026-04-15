from EFA_v2 import *
def hash_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5580136681409348930, -5185797624742061093]
    tran0.writeAction("movir X16 19824")
    tran0.writeAction("slorii X16 X16 12 2571")
    tran0.writeAction("slorii X16 X16 12 3893")
    tran0.writeAction("slorii X16 X16 12 2176")
    tran0.writeAction("slorii X16 X16 12 1346")
    tran0.writeAction("movir X17 47112")
    tran0.writeAction("slorii X17 X17 12 1416")
    tran0.writeAction("slorii X17 X17 12 2348")
    tran0.writeAction("slorii X17 X17 12 757")
    tran0.writeAction("slorii X17 X17 12 3035")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
