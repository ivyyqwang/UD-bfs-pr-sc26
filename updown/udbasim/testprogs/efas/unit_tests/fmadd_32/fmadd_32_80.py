from EFA_v2 import *
def fmadd_32_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [497534384, 358887638, 4070400281]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 29")
    tran0.writeAction("slorii X16 X16 12 2684")
    tran0.writeAction("slorii X16 X16 12 1456")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 21")
    tran0.writeAction("slorii X17 X17 12 1603")
    tran0.writeAction("slorii X17 X17 12 214")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 242")
    tran0.writeAction("slorii X18 X18 12 2518")
    tran0.writeAction("slorii X18 X18 12 281")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
