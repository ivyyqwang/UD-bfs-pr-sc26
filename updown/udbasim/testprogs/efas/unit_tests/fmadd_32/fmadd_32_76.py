from EFA_v2 import *
def fmadd_32_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [407300752, 1450858496, 2417766131]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 24")
    tran0.writeAction("slorii X16 X16 12 1134")
    tran0.writeAction("slorii X16 X16 12 2704")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 86")
    tran0.writeAction("slorii X17 X17 12 1957")
    tran0.writeAction("slorii X17 X17 12 2048")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 144")
    tran0.writeAction("slorii X18 X18 12 450")
    tran0.writeAction("slorii X18 X18 12 3827")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
