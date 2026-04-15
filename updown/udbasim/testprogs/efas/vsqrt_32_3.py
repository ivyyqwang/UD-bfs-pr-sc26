from EFA_v2 import *
def vsqrt_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2615369843, 220963886, 153210504, 3526807826, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 210")
    tran0.writeAction("slorii X19 X19 12 2980")
    tran0.writeAction("slorii X19 X19 8 46")
    tran0.writeAction("slorii X19 X19 12 2494")
    tran0.writeAction("slorii X19 X19 12 864")
    tran0.writeAction("slorii X19 X19 8 115")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3363")
    tran0.writeAction("slorii X18 X18 12 1745")
    tran0.writeAction("slorii X18 X18 8 18")
    tran0.writeAction("slorii X18 X18 12 146")
    tran0.writeAction("slorii X18 X18 12 462")
    tran0.writeAction("slorii X18 X18 8 136")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
