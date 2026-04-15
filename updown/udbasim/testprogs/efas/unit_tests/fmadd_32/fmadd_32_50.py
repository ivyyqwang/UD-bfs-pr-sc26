from EFA_v2 import *
def fmadd_32_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2054487438, 450282867, 3898754079]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 122")
    tran0.writeAction("slorii X16 X16 12 1871")
    tran0.writeAction("slorii X16 X16 12 3470")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 26")
    tran0.writeAction("slorii X17 X17 12 3436")
    tran0.writeAction("slorii X17 X17 12 1395")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 232")
    tran0.writeAction("slorii X18 X18 12 1572")
    tran0.writeAction("slorii X18 X18 12 1055")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
