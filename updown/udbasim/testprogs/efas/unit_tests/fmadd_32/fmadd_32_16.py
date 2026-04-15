from EFA_v2 import *
def fmadd_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [388520107, 504320284, 3805575894]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 23")
    tran0.writeAction("slorii X16 X16 12 645")
    tran0.writeAction("slorii X16 X16 12 2219")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 30")
    tran0.writeAction("slorii X17 X17 12 245")
    tran0.writeAction("slorii X17 X17 12 284")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 226")
    tran0.writeAction("slorii X18 X18 12 3399")
    tran0.writeAction("slorii X18 X18 12 2774")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
