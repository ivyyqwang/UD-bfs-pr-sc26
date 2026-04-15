from EFA_v2 import *
def vsub_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2897898054, 561339483, 3483067735, 1199892574, 2455696426, 323992635, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 535")
    tran0.writeAction("slorii X19 X19 12 1372")
    tran0.writeAction("slorii X19 X19 8 91")
    tran0.writeAction("slorii X19 X19 12 2763")
    tran0.writeAction("slorii X19 X19 12 2666")
    tran0.writeAction("slorii X19 X19 8 70")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1144")
    tran0.writeAction("slorii X17 X17 12 1256")
    tran0.writeAction("slorii X17 X17 8 94")
    tran0.writeAction("slorii X17 X17 12 3321")
    tran0.writeAction("slorii X17 X17 12 2917")
    tran0.writeAction("slorii X17 X17 8 87")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 308")
    tran0.writeAction("slorii X18 X18 12 4028")
    tran0.writeAction("slorii X18 X18 8 59")
    tran0.writeAction("slorii X18 X18 12 2341")
    tran0.writeAction("slorii X18 X18 12 3828")
    tran0.writeAction("slorii X18 X18 8 42")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
