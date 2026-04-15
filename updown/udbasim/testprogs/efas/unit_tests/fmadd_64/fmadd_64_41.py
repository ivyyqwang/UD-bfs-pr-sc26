from EFA_v2 import *
def fmadd_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4076428745774336981, 993876357708990637, 9755546170054914349]
    tran0.writeAction("movir X16 14482")
    tran0.writeAction("slorii X16 X16 12 1573")
    tran0.writeAction("slorii X16 X16 12 2224")
    tran0.writeAction("slorii X16 X16 12 288")
    tran0.writeAction("slorii X16 X16 12 3029")
    tran0.writeAction("movir X17 3530")
    tran0.writeAction("slorii X17 X17 12 3924")
    tran0.writeAction("slorii X17 X17 12 2067")
    tran0.writeAction("slorii X17 X17 12 3700")
    tran0.writeAction("slorii X17 X17 12 2221")
    tran0.writeAction("movir X18 34658")
    tran0.writeAction("slorii X18 X18 12 2712")
    tran0.writeAction("slorii X18 X18 12 3576")
    tran0.writeAction("slorii X18 X18 12 187")
    tran0.writeAction("slorii X18 X18 12 301")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
