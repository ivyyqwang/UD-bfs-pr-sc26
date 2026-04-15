from EFA_v2 import *
def fmadd_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9871027776724651855, 8390407714041369763, 14281207844753284179]
    tran0.writeAction("movir X16 35068")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("slorii X16 X16 12 1735")
    tran0.writeAction("slorii X16 X16 12 2812")
    tran0.writeAction("slorii X16 X16 12 3919")
    tran0.writeAction("movir X17 29808")
    tran0.writeAction("slorii X17 X17 12 2933")
    tran0.writeAction("slorii X17 X17 12 3220")
    tran0.writeAction("slorii X17 X17 12 545")
    tran0.writeAction("slorii X17 X17 12 1187")
    tran0.writeAction("movir X18 50737")
    tran0.writeAction("slorii X18 X18 12 173")
    tran0.writeAction("slorii X18 X18 12 3750")
    tran0.writeAction("slorii X18 X18 12 169")
    tran0.writeAction("slorii X18 X18 12 3155")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
