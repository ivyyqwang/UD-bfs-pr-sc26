from EFA_v2 import *
def vsub_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2413852449, 1643862763, 233309041, 1133738609, 2366999586, 1217277500, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1567")
    tran0.writeAction("slorii X19 X19 12 2906")
    tran0.writeAction("slorii X19 X19 8 235")
    tran0.writeAction("slorii X19 X19 12 2302")
    tran0.writeAction("slorii X19 X19 12 119")
    tran0.writeAction("slorii X19 X19 8 33")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1081")
    tran0.writeAction("slorii X17 X17 12 890")
    tran0.writeAction("slorii X17 X17 8 113")
    tran0.writeAction("slorii X17 X17 12 222")
    tran0.writeAction("slorii X17 X17 12 2051")
    tran0.writeAction("slorii X17 X17 8 113")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1160")
    tran0.writeAction("slorii X18 X18 12 3630")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("slorii X18 X18 12 2257")
    tran0.writeAction("slorii X18 X18 12 1420")
    tran0.writeAction("slorii X18 X18 8 34")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
