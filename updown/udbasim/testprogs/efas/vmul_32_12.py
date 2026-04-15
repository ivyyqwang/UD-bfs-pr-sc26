from EFA_v2 import *
def vmul_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2410529156, 198008699, 68295607, 796157700, 2925755648, 2770626696, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 188")
    tran0.writeAction("slorii X19 X19 12 3423")
    tran0.writeAction("slorii X19 X19 8 123")
    tran0.writeAction("slorii X19 X19 12 2298")
    tran0.writeAction("slorii X19 X19 12 3521")
    tran0.writeAction("slorii X19 X19 8 132")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 759")
    tran0.writeAction("slorii X17 X17 12 1127")
    tran0.writeAction("slorii X17 X17 8 4")
    tran0.writeAction("slorii X17 X17 12 65")
    tran0.writeAction("slorii X17 X17 12 539")
    tran0.writeAction("slorii X17 X17 8 183")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2642")
    tran0.writeAction("slorii X18 X18 12 1128")
    tran0.writeAction("slorii X18 X18 8 136")
    tran0.writeAction("slorii X18 X18 12 2790")
    tran0.writeAction("slorii X18 X18 12 893")
    tran0.writeAction("slorii X18 X18 8 0")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
