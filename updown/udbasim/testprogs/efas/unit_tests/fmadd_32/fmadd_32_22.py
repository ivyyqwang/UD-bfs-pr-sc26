from EFA_v2 import *
def fmadd_32_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1226462939, 1431397784, 2877437573]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 73")
    tran0.writeAction("slorii X16 X16 12 421")
    tran0.writeAction("slorii X16 X16 12 1755")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 85")
    tran0.writeAction("slorii X17 X17 12 1302")
    tran0.writeAction("slorii X17 X17 12 1432")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 171")
    tran0.writeAction("slorii X18 X18 12 2083")
    tran0.writeAction("slorii X18 X18 12 1669")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
