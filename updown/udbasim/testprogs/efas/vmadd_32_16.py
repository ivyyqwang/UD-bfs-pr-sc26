from EFA_v2 import *
def vmadd_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [824796313, 4207604343, 4121057099, 3947383963, 1662082109, 2299506534, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 4012")
    tran0.writeAction("slorii X19 X19 12 2802")
    tran0.writeAction("slorii X19 X19 8 119")
    tran0.writeAction("slorii X19 X19 12 786")
    tran0.writeAction("slorii X19 X19 12 2404")
    tran0.writeAction("slorii X19 X19 8 153")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3764")
    tran0.writeAction("slorii X17 X17 12 2124")
    tran0.writeAction("slorii X17 X17 8 155")
    tran0.writeAction("slorii X17 X17 12 3930")
    tran0.writeAction("slorii X17 X17 12 599")
    tran0.writeAction("slorii X17 X17 8 75")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2192")
    tran0.writeAction("slorii X18 X18 12 4015")
    tran0.writeAction("slorii X18 X18 8 102")
    tran0.writeAction("slorii X18 X18 12 1585")
    tran0.writeAction("slorii X18 X18 12 348")
    tran0.writeAction("slorii X18 X18 8 61")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
