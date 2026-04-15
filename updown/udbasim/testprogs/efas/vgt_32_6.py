from EFA_v2 import *
def vgt_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1053820620, 434926105, 790505396, 3062187663, 1417596957, 1562854680, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 414")
    tran0.writeAction("slorii X19 X19 12 3186")
    tran0.writeAction("slorii X19 X19 8 25")
    tran0.writeAction("slorii X19 X19 12 1005")
    tran0.writeAction("slorii X19 X19 12 6")
    tran0.writeAction("slorii X19 X19 8 204")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2920")
    tran0.writeAction("slorii X17 X17 12 1350")
    tran0.writeAction("slorii X17 X17 8 143")
    tran0.writeAction("slorii X17 X17 12 753")
    tran0.writeAction("slorii X17 X17 12 3623")
    tran0.writeAction("slorii X17 X17 8 180")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1490")
    tran0.writeAction("slorii X18 X18 12 1861")
    tran0.writeAction("slorii X18 X18 8 24")
    tran0.writeAction("slorii X18 X18 12 1351")
    tran0.writeAction("slorii X18 X18 12 3792")
    tran0.writeAction("slorii X18 X18 8 29")
    tran0.writeAction("vgt.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
