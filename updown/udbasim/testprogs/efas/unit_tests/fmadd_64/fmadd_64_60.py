from EFA_v2 import *
def fmadd_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6888950247105783534, 4347147707159777520, 15143127224975017479]
    tran0.writeAction("movir X16 24474")
    tran0.writeAction("slorii X16 X16 12 1916")
    tran0.writeAction("slorii X16 X16 12 34")
    tran0.writeAction("slorii X16 X16 12 326")
    tran0.writeAction("slorii X16 X16 12 1774")
    tran0.writeAction("movir X17 15444")
    tran0.writeAction("slorii X17 X17 12 700")
    tran0.writeAction("slorii X17 X17 12 3767")
    tran0.writeAction("slorii X17 X17 12 1689")
    tran0.writeAction("slorii X17 X17 12 240")
    tran0.writeAction("movir X18 53799")
    tran0.writeAction("slorii X18 X18 12 799")
    tran0.writeAction("slorii X18 X18 12 2745")
    tran0.writeAction("slorii X18 X18 12 748")
    tran0.writeAction("slorii X18 X18 12 1543")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
