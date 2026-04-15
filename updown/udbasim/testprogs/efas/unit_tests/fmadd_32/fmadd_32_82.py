from EFA_v2 import *
def fmadd_32_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [86667041, 3721918916, 2492082917]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("slorii X16 X16 12 678")
    tran0.writeAction("slorii X16 X16 12 3873")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 221")
    tran0.writeAction("slorii X17 X17 12 3455")
    tran0.writeAction("slorii X17 X17 12 2500")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 148")
    tran0.writeAction("slorii X18 X18 12 2210")
    tran0.writeAction("slorii X18 X18 12 2789")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
