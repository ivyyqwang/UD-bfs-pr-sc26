from EFA_v2 import *
def vmadd_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2119671945, 1769209532, 4225610154, 572458600, 182992653, 648529457, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1687")
    tran0.writeAction("slorii X19 X19 12 1022")
    tran0.writeAction("slorii X19 X19 8 188")
    tran0.writeAction("slorii X19 X19 12 2021")
    tran0.writeAction("slorii X19 X19 12 1952")
    tran0.writeAction("slorii X19 X19 8 137")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 545")
    tran0.writeAction("slorii X17 X17 12 3846")
    tran0.writeAction("slorii X17 X17 8 104")
    tran0.writeAction("slorii X17 X17 12 4029")
    tran0.writeAction("slorii X17 X17 12 3505")
    tran0.writeAction("slorii X17 X17 8 170")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 618")
    tran0.writeAction("slorii X18 X18 12 1990")
    tran0.writeAction("slorii X18 X18 8 49")
    tran0.writeAction("slorii X18 X18 12 174")
    tran0.writeAction("slorii X18 X18 12 2111")
    tran0.writeAction("slorii X18 X18 8 13")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
