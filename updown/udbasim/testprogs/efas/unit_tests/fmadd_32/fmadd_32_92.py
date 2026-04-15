from EFA_v2 import *
def fmadd_32_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [434611617, 1412254860, 654895786]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 25")
    tran0.writeAction("slorii X16 X16 12 3706")
    tran0.writeAction("slorii X16 X16 12 1441")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 84")
    tran0.writeAction("slorii X17 X17 12 724")
    tran0.writeAction("slorii X17 X17 12 3212")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 39")
    tran0.writeAction("slorii X18 X18 12 142")
    tran0.writeAction("slorii X18 X18 12 2730")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
