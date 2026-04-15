from EFA_v2 import *
def fmadd_32_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [225261073, 1134841131, 637469456]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 13")
    tran0.writeAction("slorii X16 X16 12 1747")
    tran0.writeAction("slorii X16 X16 12 1553")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 67")
    tran0.writeAction("slorii X17 X17 12 2628")
    tran0.writeAction("slorii X17 X17 12 3371")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 37")
    tran0.writeAction("slorii X18 X18 12 4080")
    tran0.writeAction("slorii X18 X18 12 784")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
