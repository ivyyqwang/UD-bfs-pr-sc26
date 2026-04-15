from EFA_v2 import *
def vdiv_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2945341812, 3848328950, 3653567940, 3102719487, 1912028839, 2560102003, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3670")
    tran0.writeAction("slorii X19 X19 12 214")
    tran0.writeAction("slorii X19 X19 8 246")
    tran0.writeAction("slorii X19 X19 12 2808")
    tran0.writeAction("slorii X19 X19 12 3673")
    tran0.writeAction("slorii X19 X19 8 116")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2958")
    tran0.writeAction("slorii X17 X17 12 4029")
    tran0.writeAction("slorii X17 X17 8 255")
    tran0.writeAction("slorii X17 X17 12 3484")
    tran0.writeAction("slorii X17 X17 12 1285")
    tran0.writeAction("slorii X17 X17 8 196")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2441")
    tran0.writeAction("slorii X18 X18 12 2062")
    tran0.writeAction("slorii X18 X18 8 115")
    tran0.writeAction("slorii X18 X18 12 1823")
    tran0.writeAction("slorii X18 X18 12 1854")
    tran0.writeAction("slorii X18 X18 8 167")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
