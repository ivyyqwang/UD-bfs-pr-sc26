from EFA_v2 import *
def fmadd_32_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2280702245, 642285990, 2065025697]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 135")
    tran0.writeAction("slorii X16 X16 12 3852")
    tran0.writeAction("slorii X16 X16 12 293")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 38")
    tran0.writeAction("slorii X17 X17 12 1160")
    tran0.writeAction("slorii X17 X17 12 422")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 123")
    tran0.writeAction("slorii X18 X18 12 348")
    tran0.writeAction("slorii X18 X18 12 2721")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
