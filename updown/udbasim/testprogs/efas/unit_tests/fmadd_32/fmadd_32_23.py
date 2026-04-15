from EFA_v2 import *
def fmadd_32_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1199308293, 3373306358, 2257954398]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 71")
    tran0.writeAction("slorii X16 X16 12 1983")
    tran0.writeAction("slorii X16 X16 12 3589")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 201")
    tran0.writeAction("slorii X17 X17 12 265")
    tran0.writeAction("slorii X17 X17 12 502")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 134")
    tran0.writeAction("slorii X18 X18 12 2394")
    tran0.writeAction("slorii X18 X18 12 1630")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
