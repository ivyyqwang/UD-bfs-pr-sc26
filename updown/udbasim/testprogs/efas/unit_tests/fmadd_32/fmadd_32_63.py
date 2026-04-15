from EFA_v2 import *
def fmadd_32_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2687465203, 2864006404, 2901755861]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 160")
    tran0.writeAction("slorii X16 X16 12 759")
    tran0.writeAction("slorii X16 X16 12 1779")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 170")
    tran0.writeAction("slorii X17 X17 12 2900")
    tran0.writeAction("slorii X17 X17 12 1284")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 172")
    tran0.writeAction("slorii X18 X18 12 3924")
    tran0.writeAction("slorii X18 X18 12 2005")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
