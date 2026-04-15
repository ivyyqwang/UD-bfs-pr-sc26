from EFA_v2 import *
def fmadd_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15415507747001522480, 14468911259399036630, 13340060367461669864]
    tran0.writeAction("movir X16 54766")
    tran0.writeAction("slorii X16 X16 12 3625")
    tran0.writeAction("slorii X16 X16 12 3836")
    tran0.writeAction("slorii X16 X16 12 1261")
    tran0.writeAction("slorii X16 X16 12 2352")
    tran0.writeAction("movir X17 51403")
    tran0.writeAction("slorii X17 X17 12 3682")
    tran0.writeAction("slorii X17 X17 12 383")
    tran0.writeAction("slorii X17 X17 12 529")
    tran0.writeAction("slorii X17 X17 12 3798")
    tran0.writeAction("movir X18 47393")
    tran0.writeAction("slorii X18 X18 12 1699")
    tran0.writeAction("slorii X18 X18 12 2492")
    tran0.writeAction("slorii X18 X18 12 3357")
    tran0.writeAction("slorii X18 X18 12 3048")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
