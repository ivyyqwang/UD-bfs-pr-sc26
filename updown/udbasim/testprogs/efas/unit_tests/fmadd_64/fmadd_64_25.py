from EFA_v2 import *
def fmadd_64_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9809716961788198641, 11207084532377334149, 3662066293301054483]
    tran0.writeAction("movir X16 34851")
    tran0.writeAction("slorii X16 X16 12 473")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("slorii X16 X16 12 3825")
    tran0.writeAction("movir X17 39815")
    tran0.writeAction("slorii X17 X17 12 2304")
    tran0.writeAction("slorii X17 X17 12 296")
    tran0.writeAction("slorii X17 X17 12 515")
    tran0.writeAction("slorii X17 X17 12 389")
    tran0.writeAction("movir X18 13010")
    tran0.writeAction("slorii X18 X18 12 1118")
    tran0.writeAction("slorii X18 X18 12 1068")
    tran0.writeAction("slorii X18 X18 12 576")
    tran0.writeAction("slorii X18 X18 12 3091")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
