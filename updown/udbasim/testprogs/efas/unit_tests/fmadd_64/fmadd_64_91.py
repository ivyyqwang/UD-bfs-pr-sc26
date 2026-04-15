from EFA_v2 import *
def fmadd_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10689259951278174520, 18346946453419004474, 18149604918579558550]
    tran0.writeAction("movir X16 37975")
    tran0.writeAction("slorii X16 X16 12 3604")
    tran0.writeAction("slorii X16 X16 12 2723")
    tran0.writeAction("slorii X16 X16 12 3051")
    tran0.writeAction("slorii X16 X16 12 312")
    tran0.writeAction("movir X17 65181")
    tran0.writeAction("slorii X17 X17 12 1833")
    tran0.writeAction("slorii X17 X17 12 2005")
    tran0.writeAction("slorii X17 X17 12 625")
    tran0.writeAction("slorii X17 X17 12 570")
    tran0.writeAction("movir X18 64480")
    tran0.writeAction("slorii X18 X18 12 1432")
    tran0.writeAction("slorii X18 X18 12 833")
    tran0.writeAction("slorii X18 X18 12 2527")
    tran0.writeAction("slorii X18 X18 12 2198")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
