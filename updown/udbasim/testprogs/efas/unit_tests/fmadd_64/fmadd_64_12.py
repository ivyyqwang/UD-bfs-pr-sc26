from EFA_v2 import *
def fmadd_64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6943925961662893576, 16592967810412115456, 14206263156146657894]
    tran0.writeAction("movir X16 24669")
    tran0.writeAction("slorii X16 X16 12 3197")
    tran0.writeAction("slorii X16 X16 12 3875")
    tran0.writeAction("slorii X16 X16 12 2168")
    tran0.writeAction("slorii X16 X16 12 3592")
    tran0.writeAction("movir X17 58950")
    tran0.writeAction("slorii X17 X17 12 260")
    tran0.writeAction("slorii X17 X17 12 3949")
    tran0.writeAction("slorii X17 X17 12 431")
    tran0.writeAction("slorii X17 X17 12 1536")
    tran0.writeAction("movir X18 50470")
    tran0.writeAction("slorii X18 X18 12 3217")
    tran0.writeAction("slorii X18 X18 12 655")
    tran0.writeAction("slorii X18 X18 12 3445")
    tran0.writeAction("slorii X18 X18 12 2662")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
