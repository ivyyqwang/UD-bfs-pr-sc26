from EFA_v2 import *
def vgt_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1317728304, 2268983826, 1683208346, 3643654332, 546116020, 2947728368, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2163")
    tran0.writeAction("slorii X19 X19 12 3570")
    tran0.writeAction("slorii X19 X19 8 18")
    tran0.writeAction("slorii X19 X19 12 1256")
    tran0.writeAction("slorii X19 X19 12 2800")
    tran0.writeAction("slorii X19 X19 8 48")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3474")
    tran0.writeAction("slorii X17 X17 12 3520")
    tran0.writeAction("slorii X17 X17 8 188")
    tran0.writeAction("slorii X17 X17 12 1605")
    tran0.writeAction("slorii X17 X17 12 952")
    tran0.writeAction("slorii X17 X17 8 154")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2811")
    tran0.writeAction("slorii X18 X18 12 707")
    tran0.writeAction("slorii X18 X18 8 240")
    tran0.writeAction("slorii X18 X18 12 520")
    tran0.writeAction("slorii X18 X18 12 3345")
    tran0.writeAction("slorii X18 X18 8 180")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
