from EFA_v2 import *
def fmadd_64_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13200243328395396342, 4779745559000593631, 5944115185409331595]
    tran0.writeAction("movir X16 46896")
    tran0.writeAction("slorii X16 X16 12 2805")
    tran0.writeAction("slorii X16 X16 12 3721")
    tran0.writeAction("slorii X16 X16 12 2980")
    tran0.writeAction("slorii X16 X16 12 1270")
    tran0.writeAction("movir X17 16981")
    tran0.writeAction("slorii X17 X17 12 276")
    tran0.writeAction("slorii X17 X17 12 768")
    tran0.writeAction("slorii X17 X17 12 4019")
    tran0.writeAction("slorii X17 X17 12 1247")
    tran0.writeAction("movir X18 21117")
    tran0.writeAction("slorii X18 X18 12 3028")
    tran0.writeAction("slorii X18 X18 12 1170")
    tran0.writeAction("slorii X18 X18 12 1345")
    tran0.writeAction("slorii X18 X18 12 395")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
