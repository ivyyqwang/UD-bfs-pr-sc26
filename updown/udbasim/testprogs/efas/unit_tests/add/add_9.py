from EFA_v2 import *
def add_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7946947184210240550, 9010209145392609334]
    tran0.writeAction("movir X16 28233")
    tran0.writeAction("slorii X16 X16 12 933")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 1062")
    tran0.writeAction("movir X17 32010")
    tran0.writeAction("slorii X17 X17 12 2839")
    tran0.writeAction("slorii X17 X17 12 2759")
    tran0.writeAction("slorii X17 X17 12 419")
    tran0.writeAction("slorii X17 X17 12 2102")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
