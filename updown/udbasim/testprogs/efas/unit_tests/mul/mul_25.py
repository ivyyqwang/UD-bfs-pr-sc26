from EFA_v2 import *
def mul_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4076300517534364309, -2415609414237475513]
    tran0.writeAction("movir X16 51054")
    tran0.writeAction("slorii X16 X16 12 292")
    tran0.writeAction("slorii X16 X16 12 1734")
    tran0.writeAction("slorii X16 X16 12 2552")
    tran0.writeAction("slorii X16 X16 12 3435")
    tran0.writeAction("movir X17 56954")
    tran0.writeAction("slorii X17 X17 12 128")
    tran0.writeAction("slorii X17 X17 12 2372")
    tran0.writeAction("slorii X17 X17 12 1170")
    tran0.writeAction("slorii X17 X17 12 3399")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
