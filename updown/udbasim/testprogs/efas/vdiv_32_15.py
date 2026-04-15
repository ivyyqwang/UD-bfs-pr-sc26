from EFA_v2 import *
def vdiv_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1057448120, 1029458802, 2451454836, 3588536346, 1664922677, 3054457291, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 981")
    tran0.writeAction("slorii X19 X19 12 3147")
    tran0.writeAction("slorii X19 X19 8 114")
    tran0.writeAction("slorii X19 X19 12 1008")
    tran0.writeAction("slorii X19 X19 12 1888")
    tran0.writeAction("slorii X19 X19 8 184")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3422")
    tran0.writeAction("slorii X17 X17 12 1208")
    tran0.writeAction("slorii X17 X17 8 26")
    tran0.writeAction("slorii X17 X17 12 2337")
    tran0.writeAction("slorii X17 X17 12 3643")
    tran0.writeAction("slorii X17 X17 8 116")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2912")
    tran0.writeAction("slorii X18 X18 12 3921")
    tran0.writeAction("slorii X18 X18 8 203")
    tran0.writeAction("slorii X18 X18 12 1587")
    tran0.writeAction("slorii X18 X18 12 3252")
    tran0.writeAction("slorii X18 X18 8 53")
    tran0.writeAction("vdiv.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
