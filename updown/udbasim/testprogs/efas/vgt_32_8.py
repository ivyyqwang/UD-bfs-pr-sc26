from EFA_v2 import *
def vgt_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1758086661, 1537085878, 3858102452, 352125731, 1278727908, 183384128, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1465")
    tran0.writeAction("slorii X19 X19 12 3601")
    tran0.writeAction("slorii X19 X19 8 182")
    tran0.writeAction("slorii X19 X19 12 1676")
    tran0.writeAction("slorii X19 X19 12 2630")
    tran0.writeAction("slorii X19 X19 8 5")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 335")
    tran0.writeAction("slorii X17 X17 12 3331")
    tran0.writeAction("slorii X17 X17 8 35")
    tran0.writeAction("slorii X17 X17 12 3679")
    tran0.writeAction("slorii X17 X17 12 1528")
    tran0.writeAction("slorii X17 X17 8 180")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 174")
    tran0.writeAction("slorii X18 X18 12 3640")
    tran0.writeAction("slorii X18 X18 8 64")
    tran0.writeAction("slorii X18 X18 12 1219")
    tran0.writeAction("slorii X18 X18 12 2006")
    tran0.writeAction("slorii X18 X18 8 228")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
