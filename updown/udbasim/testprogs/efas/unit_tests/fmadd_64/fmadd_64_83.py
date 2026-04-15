from EFA_v2 import *
def fmadd_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11727632363855993400, 10457060406305276403, 1228205066363743433]
    tran0.writeAction("movir X16 41664")
    tran0.writeAction("slorii X16 X16 12 3767")
    tran0.writeAction("slorii X16 X16 12 4048")
    tran0.writeAction("slorii X16 X16 12 45")
    tran0.writeAction("slorii X16 X16 12 2616")
    tran0.writeAction("movir X17 37150")
    tran0.writeAction("slorii X17 X17 12 3856")
    tran0.writeAction("slorii X17 X17 12 2336")
    tran0.writeAction("slorii X17 X17 12 2572")
    tran0.writeAction("slorii X17 X17 12 499")
    tran0.writeAction("movir X18 4363")
    tran0.writeAction("slorii X18 X18 12 1888")
    tran0.writeAction("slorii X18 X18 12 35")
    tran0.writeAction("slorii X18 X18 12 3874")
    tran0.writeAction("slorii X18 X18 12 3273")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
