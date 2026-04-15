from EFA_v2 import *
def vdiv_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [401738894, 3786106209, 1757393799, 3721494871, 2891175382, 3869770068, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3610")
    tran0.writeAction("slorii X19 X19 12 2917")
    tran0.writeAction("slorii X19 X19 8 97")
    tran0.writeAction("slorii X19 X19 12 383")
    tran0.writeAction("slorii X19 X19 12 524")
    tran0.writeAction("slorii X19 X19 8 142")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3549")
    tran0.writeAction("slorii X17 X17 12 385")
    tran0.writeAction("slorii X17 X17 8 87")
    tran0.writeAction("slorii X17 X17 12 1675")
    tran0.writeAction("slorii X17 X17 12 4019")
    tran0.writeAction("slorii X17 X17 8 135")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3690")
    tran0.writeAction("slorii X18 X18 12 2049")
    tran0.writeAction("slorii X18 X18 8 84")
    tran0.writeAction("slorii X18 X18 12 2757")
    tran0.writeAction("slorii X18 X18 12 981")
    tran0.writeAction("slorii X18 X18 8 214")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
