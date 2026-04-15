from EFA_v2 import *
def add_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8960007779948607669, 5930048228781394352]
    tran0.writeAction("movir X16 31832")
    tran0.writeAction("slorii X16 X16 12 1401")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("slorii X16 X16 12 2347")
    tran0.writeAction("slorii X16 X16 12 2229")
    tran0.writeAction("movir X17 21067")
    tran0.writeAction("slorii X17 X17 12 3127")
    tran0.writeAction("slorii X17 X17 12 513")
    tran0.writeAction("slorii X17 X17 12 1840")
    tran0.writeAction("slorii X17 X17 12 2480")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
