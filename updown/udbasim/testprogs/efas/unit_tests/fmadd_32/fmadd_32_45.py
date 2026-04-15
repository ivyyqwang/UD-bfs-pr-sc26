from EFA_v2 import *
def fmadd_32_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [328581158, 1286846164, 2085726788]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 19")
    tran0.writeAction("slorii X16 X16 12 2396")
    tran0.writeAction("slorii X16 X16 12 38")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 76")
    tran0.writeAction("slorii X17 X17 12 2875")
    tran0.writeAction("slorii X17 X17 12 1748")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 124")
    tran0.writeAction("slorii X18 X18 12 1306")
    tran0.writeAction("slorii X18 X18 12 2628")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
