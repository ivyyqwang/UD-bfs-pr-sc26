from EFA_v2 import *
def fmadd_32_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [355294178, 2389232609, 1941485474]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 21")
    tran0.writeAction("slorii X16 X16 12 725")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 142")
    tran0.writeAction("slorii X17 X17 12 1676")
    tran0.writeAction("slorii X17 X17 12 3041")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 115")
    tran0.writeAction("slorii X18 X18 12 2955")
    tran0.writeAction("slorii X18 X18 12 1954")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
