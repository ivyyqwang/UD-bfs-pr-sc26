from EFA_v2 import *
def fmadd_32_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [392019145, 4222534543, 905987326]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 23")
    tran0.writeAction("slorii X16 X16 12 1499")
    tran0.writeAction("slorii X16 X16 12 3273")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 251")
    tran0.writeAction("slorii X17 X17 12 2796")
    tran0.writeAction("slorii X17 X17 12 911")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 54")
    tran0.writeAction("slorii X18 X18 12 4")
    tran0.writeAction("slorii X18 X18 12 1278")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
