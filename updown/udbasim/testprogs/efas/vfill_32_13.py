from EFA_v2 import *
def vfill_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2349903843, 3118781100, '1.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2974")
    tran0.writeAction("slorii X18 X18 12 1234")
    tran0.writeAction("slorii X18 X18 8 172")
    tran0.writeAction("slorii X18 X18 12 2241")
    tran0.writeAction("slorii X18 X18 12 175")
    tran0.writeAction("slorii X18 X18 8 227")
    tran0.writeAction("vfill.32 X18 1.25 ")
    tran0.writeAction("yieldt")
    return efa
