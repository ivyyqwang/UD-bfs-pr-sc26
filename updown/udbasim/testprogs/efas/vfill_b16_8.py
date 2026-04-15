from EFA_v2 import *
def vfill_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [55586, 45853, 27941, 2906, '26.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 181")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 1746")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2865")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 3474")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("vfill.b16 X18 26.5 ")
    tran0.writeAction("yieldt")
    return efa
