from EFA_v2 import *
def fmadd_32_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [314260581, 1406952023, 1144945063]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 18")
    tran0.writeAction("slorii X16 X16 12 2995")
    tran0.writeAction("slorii X16 X16 12 3173")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 83")
    tran0.writeAction("slorii X17 X17 12 3526")
    tran0.writeAction("slorii X17 X17 12 599")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 68")
    tran0.writeAction("slorii X18 X18 12 999")
    tran0.writeAction("slorii X18 X18 12 2471")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
