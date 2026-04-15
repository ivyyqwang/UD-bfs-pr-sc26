from EFA_v2 import *
def fmadd_32_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [642707458, 1773237663, 3677503475]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 38")
    tran0.writeAction("slorii X16 X16 12 1263")
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 105")
    tran0.writeAction("slorii X17 X17 12 2839")
    tran0.writeAction("slorii X17 X17 12 1439")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 219")
    tran0.writeAction("slorii X18 X18 12 803")
    tran0.writeAction("slorii X18 X18 12 4083")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
