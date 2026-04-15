from EFA_v2 import *
def fmadd_32_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1498141941, 1879253512, 1227571252]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 89")
    tran0.writeAction("slorii X16 X16 12 1213")
    tran0.writeAction("slorii X16 X16 12 1269")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 112")
    tran0.writeAction("slorii X17 X17 12 50")
    tran0.writeAction("slorii X17 X17 12 520")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 73")
    tran0.writeAction("slorii X18 X18 12 692")
    tran0.writeAction("slorii X18 X18 12 52")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
