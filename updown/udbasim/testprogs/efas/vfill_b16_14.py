from EFA_v2 import *
def vfill_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12615, 62135, 8600, 35641, '57.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2227")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 537")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 3883")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 788")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vfill.b16 X18 57.25 ")
    tran0.writeAction("yieldt")
    return efa
