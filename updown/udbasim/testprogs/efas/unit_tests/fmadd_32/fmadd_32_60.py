from EFA_v2 import *
def fmadd_32_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2071398828, 502537918, 3724265161]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 123")
    tran0.writeAction("slorii X16 X16 12 1904")
    tran0.writeAction("slorii X16 X16 12 2476")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 29")
    tran0.writeAction("slorii X17 X17 12 3905")
    tran0.writeAction("slorii X17 X17 12 3774")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 221")
    tran0.writeAction("slorii X18 X18 12 4028")
    tran0.writeAction("slorii X18 X18 12 1737")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
